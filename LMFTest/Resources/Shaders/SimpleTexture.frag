#version 150
 
in vec2 UV;
in vec4 vtxColour;
out vec4 color;
uniform sampler2D myTextureSampler;
 
void main(){
    vec4 texel = texture( myTextureSampler, UV ).rgba * vtxColour;
    if (texel.a < 0.5)
        discard;
    color = texel;
}