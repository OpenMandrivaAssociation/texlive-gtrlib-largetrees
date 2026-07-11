%global tl_name gtrlib-largetrees
%global tl_revision 49062

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2b
Release:	%{tl_revision}.1
Summary:	Library for genealogytree aiming at large trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gtrlib-largetrees
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrlib-largetrees.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrlib-largetrees.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrlib-largetrees.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main goal of this package is to offer additional database fields and
formats for the genealogytree package, particularly for typesetting
large trees. The package depends on genealogytree and etoolbox.

