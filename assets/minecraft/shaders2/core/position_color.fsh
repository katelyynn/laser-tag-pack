#version 150

in vec4 vertexColor;
in float vertexDistance;
in vec3 xyzPos;

uniform float GameTime;
uniform vec4 ColorModulator;
uniform vec2 u_resolution;
uniform vec2 ScreenSize;
uniform mat4 ProjMat;

out vec4 fragColor;

void main() {
    vec4 color = vertexColor;
    if (color.a == 0.0) {
        discard;
    }

    /* slot hover colour */
    if (color.rgb == vec3(1) && color.a == 128/255.0) {
        color = vec4(0, 0, 0, 0);
    }

    /* tooltip background colour */
    if (color.r == 16/255.0 && color.g == 0/255.0 && color.b == 16/255.0 ) {
        color = vec4(0.1176, 0.1176, 0.1216, 0.8);
    }
    /* checks for border colours */
    if (color.r >= 0.15686 && color.r <= 0.31373 && color.g == 0 && color.b >= 0.49 && color.b <= 1) {
        color = vec4(0.5216, 0.5333, 0.5529, 0);
    }

    fragColor = color * ColorModulator;
}
