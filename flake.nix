{
  description = "Reproducibility in Scientific Software environment";
  inputs = {
    nixpkgs.url = "github:Nixos/nixpkgs/nixos-unstable";
  };
  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      myPythonPackages = ps: with ps; [ 
        pandas
        numpy
        matplotlib
        jupyter
        jupyter-cache
      ];
      pythonEnv = pkgs.python3.withPackages myPythonPackages;
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          ((pkgs.quarto.override {
            extraPythonPackages = myPythonPackages;
          }).overrideAttrs (oldAttrs: {
            # Remove this overrideAttrs patch when fixed.
            # See https://github.com/NixOS/nixpkgs/issues/519484#issuecomment-4667477454
            postPatch = (oldAttrs.postPatch or "") + ''
              substituteInPlace bin/quarto.js \
                --replace-fail "syntax-highlighting" "highlight-style"
            '';
          }))
          pythonEnv
        ];
        shellHook = ''
          echo "Quarto Environment Active (Pure Flake)"
          echo "Quickstart: run 'quarto render document.qmd'"
        '';
      };
    };
}
