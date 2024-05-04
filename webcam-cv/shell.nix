let
  pkgs = import <nixpkgs> { };
in
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (pp: [
      pp.numpy
      pp.requests
      # May god have mercy on my sole for this jank...
      (pp.opencv4.override { enableGtk2 = true; })
    ]))
  ];
}
