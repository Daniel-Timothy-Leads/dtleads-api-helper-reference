import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

    TEMPLATE SETTING RESTRICTIONS 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.setting_restrictions.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.setting_restrictions.get("<access_token>", "<restrictionId>") # get by id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlSettingRestrictionsCreateModel("Restriction Name") # required params
create_model.monday = [480,1020] # 9am to 5pm
create_model.tuesday = [480,1020] # 9am to 5pm
create_model.wednesday = [480,1020] # 9am to 5pm
create_model.thursday = [480] # 9am to whenever
create_model.friday = [480,1020] # 9am to 5pm

results = dtl.setting_restrictions.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlSettingRestrictionsPatchModel()
patch_model.name = "Updated Name"
patch_model.wednesday = [540, 1080]

results = dtl.setting_restrictions.patch("<access_token>", "<restrictionId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.setting_restrictions.delete("<access_token>", "<restrictionId>")
print(results.status_code) # 204 for successful request