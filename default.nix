{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python38
    pkgs.python38Packages.pip
    pkgs.python38Packages.setuptools
    pkgs.python38Packages.wheel
    pkgs.cmake
    pkgs.gcc
    pkgs.gcc11
    pkgs.libffi
    pkgs.zlib
    pkgs.libjpeg
    pkgs.libpng
    pkgs.glibc
  ];

  shellHook = ''
    export CC=gcc
    export CXX=g++
  '';
}