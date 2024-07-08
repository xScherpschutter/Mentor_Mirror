{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.opencv
    pkgs.ffmpeg
    pkgs.gtk3
    pkgs.qt5
    pkgs.libgl1
    pkgs.libgl1-mesa-glx
    pkgs.libx11
    pkgs.libxext
    pkgs.libxrender
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
