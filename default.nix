{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.mesa
    pkgs.libglvnd
    pkgs.glew
    pkgs.glfw3
    pkgs.libGLU
    pkgs.mesa_drivers
  ];

  shellHook = ''
    export LIBGL_ALWAYS_SOFTWARE=1
  '';
}
