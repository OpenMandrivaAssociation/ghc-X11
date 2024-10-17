%global debug_package %{nil}
%define module X11

Summary:	A binding to the X11 graphics library for Haskell
Name:		ghc-%{module}
Version:	1.6.0.2
Release:	3
License:	BSD
Group:		Development/Other
Url:		https://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
Requires(post,preun):	ghc

%description
A Haskell binding to the X11 graphics library.
The binding is a direct translation of the C binding; for documentation of
these calls, refer to "The Xlib Programming Manual", available online at
<http://tronche.com/gui/x/xlib/>.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

