{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python39
    pkgs.gcc
    pkgs.libgl1-mesa-glx
  ];
}