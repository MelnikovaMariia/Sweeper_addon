bl_info = {
    'name': 'Sweeper',
    'author': 'Mariia Melnikova',
    'version': (1, 0, 0),
    'blender': (2, 93, 3),
    'location': 'View 3D > UI > Sweeper',
    'description': 'Remove UV and 2nd Material',
    'warning': '',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Object'
}



import bpy 
from bpy.types import Operator, Panel, PropertyGroup
from bpy.utils import register_class, unregister_class 
from bpy.props import BoolProperty, FloatProperty, PointerProperty

def button_01(context):
        
        selected = bpy.context.selected_objects
 
        bad_uvmap_4 = 'UVMap.004' 
        bad_uvmap_5 = 'UVMap.005' 
        bad_uvmap_6 = 'UVMap.006'
 
        for obj in selected:
            try:
                badUV_4 = obj.data.uv_layers[ bad_uvmap_4 ]
                obj.data.uv_layers.remove( badUV_4 )
                badUV_5 = obj.data.uv_layers[ bad_uvmap_5 ]
                obj.data.uv_layers.remove( badUV_5 )
                badUV_6 = obj.data.uv_layers[ bad_uvmap_6 ]
                obj.data.uv_layers.remove( badUV_6 )
                
            except:
             pass   
         
class OBJECT_OT_Apply_All_Op(Operator): 
    bl_idname = 'object.apply_all_mods'
    bl_label = 'Apply all' 
    bl_description = 'Apply all operators of the active object'
                
    def execute(self, context):            
        button_01(context)
        return {'FINISHED'} 
    
    
def button_02(context):
        
    bpy.ops.object.material_slot_remove_unused()
         
class OBJECT_OT_Remove_Material(Operator): 
    bl_idname = 'object.remove_material'
    bl_label = 'Apply' 
    bl_description = 'Remove Material'
                
    def execute(self, context):            
        button_02(context)
        return {'FINISHED'}     
    
    
class OBJECT_PT_Remove_UV(bpy.types.Panel):
    bl_idname = 'object.removeuv'
    bl_label = 'Remove UV'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI' 
    bl_category = 'Sweeper'
   
     
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column()
        col.operator('object.apply_all_mods', text='Apply all')
        
        
class OBJECT_PT_Remove_Material(bpy.types.Panel):
    bl_idname = 'object.removematerial'
    bl_label = 'Remove Material'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI' 
    bl_category = 'Sweeper'
   
     
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column()
        col.operator('object.remove_material', text='Apply all')
        
       
    
    

class CleanProps(PropertyGroup):
    remove_UV : BoolProperty(
        name = 'Remove UV',
        default = True
    )


classes = [
    OBJECT_PT_Remove_UV, 
    CleanProps,
    OBJECT_OT_Apply_All_Op,
    OBJECT_OT_Remove_Material,
    OBJECT_PT_Remove_Material   
]
            
def register(): 
    for c in classes:
        bpy.utils.register_class(c)
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    
if __name__ == '__main__':
    register() 
    
    
    @classmethod
    def poll(cls, context):
        obj = context.object
        
        if obj is not None:
            if obj.mode == 'OBJECT':
                return True 
            return False
