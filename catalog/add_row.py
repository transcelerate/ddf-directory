# Standard Library Imports
import os
import json

# Define constants
CATALOG_PATH = r'catalog/catalog.md'

def transform_use_cases(use_cases: str) -> str:
    '''Function for discarding any use cases that were not selected.'''
    use_cases = use_cases.strip()

    use_cases_selected = [value.strip('- [X] ') for value in use_cases.split('\n') if "[X]" in value]

    return ', '.join(use_cases_selected)

def transform_email_address(email: str) -> str:
    '''Function for converting an email address into a mailto: link string in the markdown format.'''
    email = f'[Email](mailto:{email})'
    return email

def append_other_use_cases(use_cases: str, other_use_cases: str) -> str:
    '''Function for appending any freetext use cases to the "Covered Ue Cases" field, discarding the "Other(s)" option, if selected.'''
    if use_cases == '_No response_':
        use_cases = other_use_cases
        pass
    else:
        use_cases += ', ' + other_use_cases
    
    return use_cases

def format_link_markdown(input_link: str, label:str) -> str:
    '''Function for formating as link in markdown format with a custom label.'''
    return f'[{label}]({input_link})'

def transform_insert_dict(insert_dict: dict[str, str], issue_url):
    '''Function for performing all transformations to the insert_dictionary'''
    # Remove secondary email and confirm submission from insert dict, as we don't write that to the table
    del insert_dict["Secondary Point of Contact Email"]
    del insert_dict['Confirm Submission?']

    # Format Email as mailto: in markdown format
    insert_dict['Primary Point of Contact Email'] = transform_email_address(insert_dict['Primary Point of Contact Email'])

    # Truncate 'Product Short Description' to 250 characters
    insert_dict["Product Short Description"] = insert_dict['Product Short Description'][0:250]

    # Transform 'Product Long Description'
    insert_dict['Product Long Description'] = format_link_markdown(issue_url, label='More Information')

    # Discard non-selected use cases
    insert_dict['Covered Use Cases'] = transform_use_cases(insert_dict['Covered Use Cases'])

    # Process Other Uses Case(s)
    if insert_dict['Other Use Case(s)'] != '_No response_':
        insert_dict['Covered Use Cases'] = append_other_use_cases(insert_dict['Covered Use Cases'], insert_dict['Other Use Case(s)'])

    # Transform external link
    if insert_dict['Link to Product Website'] != '_No response_':
        insert_dict['Link to Product Website'] = format_link_markdown(insert_dict['Link to Product Website'], label='LINK')
    else:
        insert_dict['Link to Product Website'] = ''

    # Delete 'Other Use Case(s)' from insert_dict
    del insert_dict['Other Use Case(s)']

    return insert_dict

def write_to_catalog(insert_dict: dict[str, str])-> None:
    '''Function to convert the insert_dict into a markdown table row and write it to file.'''
    # Convert dictionary values to list
    insert_list = list(insert_dict.values())

    # Transform list into pip delimited string, for insertion into markdown table
    insert_row = '| ' + ' | '.join(insert_list) + ' |'

    # Open catalog.md and write row to bottom of file
    with open(CATALOG_PATH, 'r+') as fin:
        lines = fin.read()
        if lines[-1] in ['\n', '\r\n', '']:
            fin.write(insert_row)
        else: 
            fin.write('\n'+insert_row)

def main():
    '''Main function, transforms payload into a markdown table formatted string and inserts it to the catalog.md file.'''
    # Store github_issue_context payload as python dictionary
    payload_dict: dict = json.loads(os.environ['GITHUB_CONTEXT'])

    # Extract Issue content from JSON Dictionary
    issue_body: list = payload_dict["body"].split('###')[1:]
    issue_url: str = payload_dict["html_url"]

    # Compose ordered dictionary of form answer : responses
    insert_dict = {key:value for key, value in [item.strip().split('\n\n') for item in issue_body]}

    # Perform all insert_dict transformations
    insert_dict = transform_insert_dict(insert_dict, issue_url)

    write_to_catalog(insert_dict)

if __name__ == "__main__":
    main()