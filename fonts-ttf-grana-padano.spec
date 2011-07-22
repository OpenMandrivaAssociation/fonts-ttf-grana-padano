%define pkgname grana-padano

Summary: medium-weight upright sans-serif font
Name: fonts-ttf-grana-padano
Version: 20100429
Release: %mkrel 1
License: OFL
Group: System/Fonts/True type
URL: http://io.debian.net/~danielj/
Source0: http://io.debian.net/~danielj/grana-padano/%{pkgname}-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: freetype-tools
BuildRequires: fontforge

%description
Grana Padano is a medium-weight upright sans-serif font in roughly the same family as Apple Computer’s historic Chicago font. It has support for Latin and Cyrillic character sets, containing sufficient characters for Latin-0 through Latin-10, as well as support for Vietnamese and all major Slavic Cyrillic-based languages.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build
for sfdfile in *.sfd
do
  fontforge -c "Open(\"$sfdfile\")
    Generate(\"$sfdfile\":r + \".ttf\")"
done

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/grana-padano

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/grana-padano
ttmkfdir %{buildroot}%{_xfontdir}/TTF/grana-padano > %{buildroot}%{_xfontdir}/TTF/grana-padano/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/grana-padano/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/grana-padano \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-grana-padano:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FONTLOG.txt
%dir %{_xfontdir}/TTF/grana-padano
%{_xfontdir}/TTF/grana-padano/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/grana-padano/fonts.dir
%{_xfontdir}/TTF/grana-padano/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-grana-padano:pri=50



