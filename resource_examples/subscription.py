import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

      SUBSCRIPTION 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.subscription.get("<access_token>")
details = dtl.handle_response(results)
print(details)
