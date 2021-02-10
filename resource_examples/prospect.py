import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

        PROSPECT 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.prospects.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.prospects.get("<access_token>", "<prospectId>") # get by Id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlProspectCreateModel("<companyId>") # requred param
create_model.first_name = ""
create_model.last_name = ""
create_model.title = ""
create_model.email = ""

results = dtl.prospects.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlProspectPatchModel()
patch_model.first_name = ""
patch_model.last_name = ""
patch_model.email = ""
patch_model.title = ""
patch_model.company_id = ""

results = dtl.prospects.patch("<access_token>", "<prospectId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.prospects.delete("<access_token>", "<prospectId>")
print(results.status_code) # 204 for successful request