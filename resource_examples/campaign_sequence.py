import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

    CAMPAIGN SEQUENCE
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.campaign_sequences.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.campaign_sequences.get("<access_token>", "<campaignId>", "<prospectId>") # get by Id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlCampaignSequenceCreateModel("<campaignId>", "<prospectId>")
create_model.index_order = 0

results = dtl.campaign_sequences.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlCampaignSequencePatchModel()
patch_model.index_order = 0

results = dtl.campaign_sequences.patch("<access_token>", "<campaignId>", "<prospectId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.campaign_sequences.delete("<access_token>", "<campaignId>", "<prospectId>")
print(results.status_code) # 204 for successful request