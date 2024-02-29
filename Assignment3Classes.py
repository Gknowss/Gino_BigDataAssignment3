class plot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def make(self):    
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm

        # Setup subplot and cmap to organize
        fig, ax = plt.subplots()

        #Setup values for x and y
        idx = self.x.classes
        counts = self.y.types

        # Decorate plot
        length = len(idx)
        cmap = cm.get_cmap('plasma', length)

        # For every thing in class, match with calculated y values of usage
        i = 0 
        for key, value in zip(idx, counts):
            if (value > 0):
                ax.bar(key, value, label=key, color = cmap(i))
                i = i + 1
        
        # Now to actually fill in the plot details        
        plt.title('Most Popular Classes')
        plt.ylabel('Usage')
        plt.xlabel('Class')
        plt.xticks(rotation=90)
        plt.legend(bbox_to_anchor=(1.5,1),loc='upper right')
        plt.show()
        plt.close()
        
class agr:
    def __init__(self, var):
        self.var = var
    
    def aggregate(self):
        import redis
        from db_config import get_redis_connection
        import redis.commands.search.aggregation as aggregations
        from redis.commands.search.field import TextField, NumericField, TagField
        from redis.commands.search.indexDefinition import IndexDefinition, IndexType
        import redis.commands.search.reducers as reducers
        
        # Get redis Connection
        r = get_redis_connection()
        
        # Create fields for which data is to be aggregated
        schema = (
            TextField("$.sets", as_name="sets"), 
            TagField("$.standard", as_name="standard"), 
            NumericField("$.wild", as_name="wild")
        )
        
        # Make index to use aggregation commands built in Python
        rs = r.ft("idx:sets")
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=["date:"], index_type=IndexType.JSON
            )
        )
        # Aggregate
        req = aggregations.AggregateRequest("*").group_by('@city', reducers.count().alias('count'))
        print(rs.aggregate(req).rows)

class basic:
    def __init__(self, var):
        self.var = var
        
    def query(self):
        import redis
        from db_config import get_redis_connection
        from redis.commands.search.field import TextField, NumericField, TagField
        from redis.commands.search.indexDefinition import IndexDefinition, IndexType
        
        # Connect to redis, and get a basic search
        r = get_redis_connection()
        r.get('sets')
        
        