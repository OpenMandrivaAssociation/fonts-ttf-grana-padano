%define fontname grana-padano

Summary:	medium-weight upright sans-serif font
Name:		fonts-ttf-grana-padano
Version:	20100429
Release:	3
License:	OFL
Group:		System/Fonts/True type
Url:		http://io.debian.net/~danielj/
Source0:	http://io.debian.net/~danielj/grana-padano/%{fontname}-%{version}.zip
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	fontforge

%description
Grana Padano is a medium-weight upright sans-serif font in roughly the same
family as Apple Computer’s historic Chicago font. It has support for Latin and
Cyrillic character sets, containing sufficient characters for Latin-0 through
Latin-10, as well as support for Vietnamese and all major Slavic
Cyrillic-based languages.

%files
%doc FONTLOG.txt
%dir %{_xfontdir}/TTF/grana-padano
%{_xfontdir}/TTF/grana-padano/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/grana-padano/fonts.dir
%{_xfontdir}/TTF/grana-padano/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-grana-padano:pri=50

#----------------------------------------------------------------------------

%prep
%setup -q -c -n %{fontname}-%{version}

%build
for sfdfile in *.sfd
do
  fontforge -lang=ff -c "Open(\"./$sfdfile\"); Generate(\"./$sfdfile\":r + \".ttf\")"
done

%install
mkdir -p %{buildroot}%{_xfontdir}/TTF/grana-padano

install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/grana-padano
ttmkfdir %{buildroot}%{_xfontdir}/TTF/grana-padano > %{buildroot}%{_xfontdir}/TTF/grana-padano/fonts.dir
ln -s fonts.dir %{buildroot}%{_xfontdir}/TTF/grana-padano/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_xfontdir}/TTF/grana-padano \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-grana-padano:pri=50

