import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper

## Authentication/Authorization
results = dtl.authorize_login("<username>", "<password>")
token_details = dtl.handle_response(results)
print(token_details)

## refresh the token
refresh_token = token_details['refresh_token']
results = dtl.refresh_token(refresh_token)
token_details = dtl.handle_response(results)
print(token_details)