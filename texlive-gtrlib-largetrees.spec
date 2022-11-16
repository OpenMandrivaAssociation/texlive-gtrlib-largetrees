Name:		texlive-gtrlib-largetrees
Version:	49062
Release:	1
Summary:	Library for genealogytree aiming at large trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gtrlib-largetrees
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrlib-largetrees.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrlib-largetrees.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gtrlib-largetrees.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The main goal of this package is to offer additional database
fields and formats for the genealogytree package, particularly
for typesetting large trees. The package depends on
genealogytree and etoolbox.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gtrlib-largetrees
%{_texmfdistdir}/tex/latex/gtrlib-largetrees
%doc %{_texmfdistdir}/doc/latex/gtrlib-largetrees

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
