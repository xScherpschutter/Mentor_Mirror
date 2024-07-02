{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python38
    python38Packages.pip
    python38Packages.setuptools
    python38Packages.wheel
    cmake
    gcc
    gcc11
    libffi
    zlib
    libjpeg
    libpng
    glibc
    python38Packages.cffi
    python38Packages.python38-openssl
    python38Packages.python38-dev
    libX11.dev
  ];
}
