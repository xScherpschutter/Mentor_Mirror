{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.opencv
    pkgs.ffmpeg
    pkgs.gtk3
    pkgs.qt5
    pkgs.mesa
    pkgs.libGL
    pkgs.libGL1
    pkgs.libX11
    pkgs.libXext
    pkgs.libXrender
    pkgs.libxcb
    pkgs.gstreamer
    pkgs.gst-plugins-base
    pkgs.gst-plugins-good
    pkgs.gst-plugins-bad
    pkgs.gst-plugins-ugly
    pkgs.gst-libav
    pkgs.openexr
    pkgs.zlib
    pkgs.libpng
    pkgs.libjpeg
    pkgs.libtiff
    pkgs.eigen
    pkgs.tbb
    pkgs.cudatoolkit
    pkgs.ipp
  ];
}
