{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.libglvnd
    pkgs.libglvnd.override { mesa_drivers = [ pkgs.mesa_drivers ]; }
    pkgs.libglfw
    pkgs.mesa
  ];
  }