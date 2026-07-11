%global tl_name cleanthesis
%global tl_revision 51472

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4.0
Release:	%{tl_revision}.1
Summary:	A clean LaTeX style for thesis documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cleanthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleanthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleanthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers a clean, simple, and elegant LaTeX style for thesis
documents.

