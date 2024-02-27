class plot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def make(self):    
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm

        fig, ax = plt.subplots()

        idx = self.x.sunrise
        counts = self.y.sunset

        length = len(idx)
        cmap = cm.get_cmap('plasma', length)

        i = 0 
        for key, value in zip(idx, counts):
            if (value > 0):
                ax.bar(key, value, label=key, color = cmap(i))
                i = i + 1
                
        plt.title('Longest Days of Sun ($)')
        plt.ylabel('Time Of Sun')
        plt.xlabel('Date')
        plt.xticks(rotation=90)
        plt.legend(bbox_to_anchor=(1.5,1),loc='upper right')
        plt.show()
        plt.close()
        
class agr:
    def __init__(self, var):
        self.var = var
    
    def aggregate(self):
        import redis
        import redis.commands.search.aggregation as aggregations
        from redis.commands.search.field import TextField, NumericField, TagField
        from redis.commands.search.indexDefinition import IndexDefinition, IndexType
        import redis.commands.search.reducers as reducers
        
        #
        r = redis.Redis(host='localhost', port=6379)
        #
        schema = (
            TextField("$.name", as_name="name"), 
            TagField("$.city", as_name="city"), 
            NumericField("$.age", as_name="age")
        )
        #
        rs = r.ft("idx:date")
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=["date:"], index_type=IndexType.JSON
            )
        )
        req = aggregations.AggregateRequest("*").group_by('@city', reducers.count().alias('count'))
        print(rs.aggregate(req).rows)

class basic:
    def __init__(self, var):
        self.var = var
        
    def query(self):
        import redis
        from redis.commands.search.field import TextField, NumericField, TagField
        from redis.commands.search.indexDefinition import IndexDefinition, IndexType
        
        #
        r = redis.Redis(host='localhost', port=6379)
        #
        schema = (
            TextField("$.name", as_name="name"), 
            TagField("$.city", as_name="city"), 
            NumericField("$.age", as_name="age")
        )
        #
        rs = r.ft("idx:users")
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=["user:"], index_type=IndexType.JSON
            )
        )
        #
        
        