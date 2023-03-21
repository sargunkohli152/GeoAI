#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -U leafmap geopandas')


# In[3]:


import leafmap
import geopandas as gpd


# In[4]:


leafmap.maxar_collections()


# In[5]:


collection = 'Kahramanmaras-turkey-earthquake-23'
url = leafmap.maxar_collection_url(collection, dtype='geojson')
url


# In[6]:


gdf = gpd.read_file(url)
print(f'Total number of images: {len(gdf)}')
gdf.head()


# In[7]:


m = leafmap.Map()
m.add_gdf(gdf, layer_name='Footprints')
m


# In[8]:


pre_gdf = leafmap.maxar_search(collection, end_date='2023-02-06')
print(f'Total number of pre-event images: {len(pre_gdf)}')
pre_gdf.head()


# In[9]:


post_gdf = leafmap.maxar_search(collection, start_date='2023-02-06')
print(f'Total number of post-event images: {len(post_gdf)}')
post_gdf.head()


# In[10]:


m = leafmap.Map()
pre_style = {'color': 'red', 'fillColor': 'red', 'opacity': 1, 'fillOpacity': 0.5}
m.add_gdf(pre_gdf, layer_name='Pre-event', style=pre_style, info_mode='on_click')
m.add_gdf(post_gdf, layer_name='Post-event', info_mode='on_click')
m


# In[11]:


bbox = m.user_roi_bounds()
if bbox is None:
    bbox = [36.8715, 37.5497, 36.9814, 37.6019]


# In[12]:


pre_event = leafmap.maxar_search(collection, bbox=bbox, end_date='2023-02-06')
pre_event.head()


# In[13]:


post_event = leafmap.maxar_search(collection, bbox=bbox, start_date='2023-02-06')
post_event.head()


# In[14]:


pre_tile = pre_event['catalog_id'].values[0]
pre_tile


# In[15]:


post_tile = post_event['catalog_id'].values[0]
post_tile


# In[16]:


pre_stac = leafmap.maxar_tile_url(collection, pre_tile, dtype='json')
pre_stac


# In[17]:


post_stac = leafmap.maxar_tile_url(collection, post_tile, dtype='json')
post_stac


# In[18]:


import leafmap.foliumap as leafmap


# In[23]:


m = leafmap.Map()
m.split_map(
    left_layer=pre_stac,
    right_layer=post_stac,
    left_label='Pre-event',
    right_label='Post-event',
)
m.set_center(36.9265, 37.5762, 16)
m


# In[25]:


pre_images = pre_event['visual'].tolist()
post_images = post_event['visual'].tolist()


# In[26]:


leafmap.maxar_download(pre_images)


# In[27]:


leafmap.maxar_download(pre_images)


# In[ ]:




