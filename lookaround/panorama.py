class LookaroundPanorama:
    def __init__(self, panoid, region_id, lat, lon):
        self.panoid = panoid
        self.region_id = region_id
        self.lat = lat
        self.lon = lon

        self.date = None
        
        self.heading = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.panoid}/{self.region_id} ({self.lat:.6}, {self.lon:.6}) " \
               f"[{self.date.strftime('%Y-%m-%d')}]"
