from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.list import ILeftBody, OneLineAvatarListItem
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button  import MDRectangleFlatIconButton, MDFillRoundFlatIconButton
from kivy.uix.boxlayout import BoxLayout
import fiona as f
from kivy.uix.button import Button
from kivy.config import Config


class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()

class CustomNavigationDrawerIconButton(OneLineAvatarListItem):
    source = StringProperty()

    def _set_active(self, active, nav_drawer):
        pass

class ContentNavigationDrawer(BoxLayout):
    pass

class Tools(BoxLayout):
    pass 

class NavigationItem(OneLineAvatarListItem):
    icon = StringProperty()
class MainApp(MDApp):
    def build(self):
        #theme_cls=ThemeManager()
#         theme_cls.primary_palette="Green
        self.icon='C:\\Users\\emcfm\\Downloads\\DigitalCopy_MarketHospital.jpg'
        self.title="Angola Map"
        return Builder.load_file("kvdm/tools.kv")
    
    def on_start(self):
        print("esssss")
        files=f.open("C:\\Users\\EzequielMussambe\\Downloads\\angola\\angola-latest-free.shp\\gis_osm_pois_free_1.shp")
            #"C:/Users/emcfm/Downloads/Angola/gis_osm_pois_free_1.shp")
        for s in files:
            if s["properties"]["fclass"].lower()=="hospital" or s["properties"]["fclass"].lower()=="doctors":
            
                box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
                s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
                md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='hospital')
             
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                marks.add_widget(box)
                self.root.ids.maps_hos.add_widget(marks)

            elif s["properties"]["fclass"].lower()=="school" or s["properties"]["fclass"].lower()=="university" or s["properties"]["fclass"].lower()=="college":
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
                s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
                md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='school')
             
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                marks.add_widget(box)
                self.root.ids.maps_sch.add_widget(marks)

            elif s["properties"]["fclass"].lower()=="bank":
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
                s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
                md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='bank')
             
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                marks.add_widget(box)
                self.root.ids.maps_ban.add_widget(marks)

            elif s["properties"]["fclass"].lower()=="supermarket" or s["properties"]["fclass"].lower()=="department_store":
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
                s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
                md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='store')
             
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                marks.add_widget(box)
                self.root.ids.maps_com.add_widget(marks)

            elif s["properties"]["fclass"].lower()=="hotel":
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                box=MDFillRoundFlatIconButton(text="Class Name: {}\nName: {}\nCordinates: {} , {}".format(s["properties"]["fclass"],
                s["properties"]["name"],s["geometry"]['coordinates'][1],s["geometry"]['coordinates'][0]), 
                md_bg_color=[0,0,0,1], text_color=[0,0,0,1],size_hint=(None, 1),width=200, icon='city')
             
                marks=MapMarkerPopup(lat=s["geometry"]['coordinates'][1],lon=s["geometry"]['coordinates'][0])
                marks.add_widget(box)
                self.root.ids.maps_hou.add_widget(marks)

    def zoom_in_level(self):
        self.root.ids.homes.zoom +=1
        self.root.ids.maps_hos.zoom +=1
        self.root.ids.maps_sch.zoom +=1
        self.root.ids.maps_ban.zoom +=1
        self.root.ids.maps_com.zoom +=1
        self.root.ids.maps_hou.zoom +=1

    def zoom_out_level(self):
        self.root.ids.homes.zoom -=1
        self.root.ids.maps_hos.zoom -=1
        self.root.ids.maps_sch.zoom -=1
        self.root.ids.maps_ban.zoom -=1
        self.root.ids.maps_com.zoom -=1
        self.root.ids.maps_hou.zoom -=1
if __name__ == "__main__":
    MainApp().run()



# KV = '''
# #:import IconLeftWidget kivymd.uix.list.IconLeftWidget
# #:import images_path kivymd.images_path


# <NavigationItem>
#     theme_text_color: 'Custom'
#     divider: None

#     IconLeftWidget:
#         icon: root.icon

# <ContentNavigationDrawer>
   
#     BoxLayout:
#         orientation: 'vertical'

#         FloatLayout:
#             size_hint_y: None
#             height: "200dp"

#             canvas:
#                 Color:
#                     rgba: app.theme_cls.primary_color
#                 Rectangle:
#                     pos: self.pos
#                     size: self.size

#             BoxLayout:
#                 id: top_box
#                 size_hint_y: None
#                 height: "200dp"
#                 #padding: "10dp"
#                 x: root.parent.x
#                 pos_hint: {"top": 1}

#                 FitImage:
#                     source: f"{images_path}kivymd_alpha.png"

#             MDIconButton:
#                 icon: "close"
#                 x: root.parent.x + dp(10)
#                 pos_hint: {"top": 1}
#                 on_release: root.parent.toggle_nav_drawer()

#             MDLabel:
#                 markup: True
#                 text: "[b]KivyMD[/b]\\nVersion: 0.102.1"
#                 #pos_hint: {'center_y': .5}
#                 x: root.parent.x + dp(10)
#                 y: root.height - top_box.height + dp(10)
#                 size_hint_y: None
#                 height: self.texture_size[1]

#         ScrollView:
#             pos_hint: {"top": 1}

#             GridLayout:
#                 id: box_item
#                 cols: 1
#                 size_hint_y: None
#                 height: self.minimum_height


# Screen:

#     NavigationLayout:

#         ScreenManager:

#             Screen:

#                 BoxLayout:
#                     orientation: 'vertical'

#                     MDToolbar:
#                         title: "Navigation Drawer"
#                         md_bg_color: app.theme_cls.primary_color
#                         elevation: 10
#                         left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                   
#                     MapView:
#                         id:mains
#                         lat:36.000
#                         lon:-30.000
#                         zoom:2
#                         double_tap_zoom:True

#         MDNavigationDrawer:
#             id: nav_drawer

#             ContentNavigationDrawer:
#                 id: content_drawer

# '''


# class ContentNavigationDrawer(BoxLayout):
#     pass


# class NavigationItem(OneLineAvatarListItem):
#     icon = StringProperty()


# class TestNavigationDrawer(MDApp):
#     def build(self):
#         return Builder.load_string(KV)

#     def on_start(self):
#         for items in {
#             "home-circle-outline": "Home",
#             "update": "Check for Update",
#             "settings-outline": "Settings",
#             "exit-to-app": "Exit",
#         }.items():
#             self.root.ids.content_drawer.ids.box_item.add_widget(
#                 NavigationItem(
#                     text=items[1],
#                     icon=items[0],
#                 )
#             )


# TestNavigationDrawer().run()
