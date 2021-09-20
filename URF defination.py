#URF defination
#URF->tuple(Status,Content)
#Status->True/False
#Content->Return package/Error msg
#When ok: return package should be a dict can be used in **kwargs
#When Fatal: return should be dict{}(Recommend keys contain "msg"(hint) and "detail"(some status value(variants) of the function)_