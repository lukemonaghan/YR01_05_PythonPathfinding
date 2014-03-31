#version 150
#extension GL_ARB_explicit_attrib_location: enable

layout(location = 0) in vec3 vertexPosition_modelspace;
layout(location = 1) in vec2 vertexUV;
layout(location = 2) in vec4 vertexColour;

out vec2 UV;
out vec4 vtxColour;
uniform mat4 MVP;
 
void main(){
    gl_Position =  MVP * vec4(vertexPosition_modelspace,1);
    UV = vertexUV;
    vtxColour = vertexColour;
}