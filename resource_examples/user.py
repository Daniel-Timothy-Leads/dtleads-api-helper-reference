import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

        USER 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.users.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.users.get("<access_token>", "<userId>") # get by id
details = dtl.handle_response(results)
print(details)

##
## UPDATE
##
patch_model = dtl_models.DtlUserPatchModel()
patch_model.first_name = ""
patch_model.last_name = ""

results = dtl.users.patch("<access_token>", "<userId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)