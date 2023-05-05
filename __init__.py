import bpy
import os
import sys
import subprocess

# 定义Blender插件信息
bl_info = {
    "name": "My HairNet",
    "description": "Description of my plugin",
    "author": "kiana",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "View3D > Tools",
    "warning": "",
    "category": "Development",
}


# 安装配置环境
def env_install():
    python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
    target = os.path.join(sys.prefix, 'lib', 'site-packages')

    # upgrade pip
    subprocess.call([python_exe, '-m', 'ensurepip'])
    subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'pip'])

    # install package
    subprocess.call([python_exe, '-m', 'pip', 'install', '--upgrade', 'opencv-python', '-t', target])

# 执行main.py的函数
def run_main():
    plugin_dir = os.path.dirname(os.path.realpath(__file__))
    main_file = os.path.join(plugin_dir, "network/src/main.py")
    exec(compile(open(main_file).read(), main_file, 'exec'))



# 定义Blender操作面板
class MyPanel(bpy.types.Panel):
    bl_label = "HairNet"
    bl_idname = "OBJECT_PT_my_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "HN"

    def draw(self, context):
        layout = self.layout
        # 按钮：配置环境
        layout.operator("my_plugin.env_install", text="Install Environment")
        # 按钮：执行main.py
        layout.operator("my_plugin.run_main", text="Run Main")

class RunMainOperator(bpy.types.Operator):
    bl_idname = "my_plugin.run_main"
    bl_label = "Run Main"

    def execute(self, context):
        run_main()
        return {'FINISHED'}

class EnvInstallOperator(bpy.types.Operator):
    bl_idname = "my_plugin.env_install"
    bl_label = "Install Environment"

    def execute(self, context):
        env_install()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(MyPanel)
    bpy.utils.register_class(EnvInstallOperator)
    bpy.utils.register_class(RunMainOperator)

def unregister():
    bpy.utils.unregister_class(MyPanel)
    bpy.utils.unregister_class(EnvInstallOperator)
    bpy.utils.unregister_class(RunMainOperator)

if __name__ == "__main__":
    register()
