import influxdb_client

import libs.tokens as tokens

# from(bucket: "crypto")
#   |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
#   |> filter(fn: (r) => r["_measurement"] == "XRP-USD")
#   |> filter(fn: (r) => r["_field"] == "price")
#   |> aggregateWindow(every: 4h, fn: mean, createEmpty: false)
#   |> yield(name: "mean")

def get_data(syms, fields=["open", "high", "low", "close","volume", "price"], url="http://192.168.0.19:8086", bucket="crypto", org="fef",start="-4000d",stop="0",agg_dur=None,agg_fn=None):
    client = influxdb_client.InfluxDBClient(url=url, token=tokens.IFD_TOKEN,org=org)
    query = client.query_api()
    data = {}

    if stop == "0":
        stop = "now()"

    for idx, sym in enumerate(syms):
        
        _data = {}
        queries = []
        for f in fields:
            query_txt = f"from(bucket: \"{bucket}\") |> range(start: {start}, stop: {stop})|>filter(fn: (r)=> r._measurement==\"{sym}\" and r._field==\"{f}\")"

            if agg_fn and agg_dur:
                query_txt += f"|> aggregateWindow(every: {agg_dur}, fn: {agg_fn}, createEmpty: false) "

            queries.append(query_txt)

            stream = query.query_stream(org=org,query=query_txt)
            
            raw = [(s.get_value(),s.get_time()) for s in stream]

            _data[f] = [r[0] for r in raw]
    
            _data["time_"+f] = [r[1] for r in raw]

        data[sym] = _data
        return data, queries

def get_data_single(sym, fields=["open", "high", "low", "close","volume","price"], url="http://192.168.0.19:8086", bucket="crypto", org="fef",start="-4000d",stop="0", agg_dur=None, agg_fn=None):
    client = influxdb_client.InfluxDBClient(url=url, token=tokens.IFD_TOKEN,org=org)
    query = client.query_api()
    data = {}

    if stop == "0":
        stop = "now()"

    
        
    _data = {}
    queries = []
    for f in fields:
        query_txt = f"from(bucket: \"{bucket}\") |> range(start: {start}, stop: {stop})|>filter(fn: (r)=> r._measurement==\"{sym}\" and r._field==\"{f}\")"
        if agg_fn and agg_dur:
                query_txt += f"|> aggregateWindow(every: {agg_dur}, fn: {agg_fn}, createEmpty: false) "
        queries.append(query_txt)

        stream = query.query_stream(org=org,query=query_txt)
        
        raw = [(s.get_value(),s.get_time()) for s in stream]

        _data[f] = [r[0] for r in raw]
        _data["time_"+f] = [r[1] for r in raw]
     
    
    return _data, queries


