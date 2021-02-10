import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

        CAMPAIGN
    RESOURCE EXAMPLE

'''

##
## VIEW
##
results = dtl.campaigns.get("<access_token>") # all results
details = dtl.handle_response(results)
print(details)

results = dtl.campaigns.get("<access_token>", "<campaignId") # find by id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlCampaignCreateModel("<companyId>", "<templateId>")
create_model.OnReplyAction = "PAUSE" # PAUSE, NEXT, CONTINUE  (default = PAUSE)
create_model.ScheduledMailLimit = 1 # 1-200 limit (default = 1)

results = dtl.campaigns.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlCampaignPatchModel()
patch_model.template_id = "<templateId>" # change email template 
patch_model.OnReplyAction = "NEXT"
patch_model.ScheduledMailLimit = 2

results = dtl.campaigns.patch("<access_token>", "<campaignId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.campaigns.delete("<access_token>", "<campaignId>")
results = dtl.handle_response(results)
print(results.status_code) # 204 for successful request


##
## TURN ON
##
results = dtl.campaigns.turn_on("<access_token>", "<campaignId>")
details = dtl.handle_response(results)
print(details)


##
## TURN OFF
##
results = dtl.campaigns.turn_off("<access_token>", "<campaignId>")
details = dtl.handle_response(results)
print(details)