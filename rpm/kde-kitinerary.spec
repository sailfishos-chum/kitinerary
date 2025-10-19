%global pkgname kitinerary
%global kde_version 25.08.2
%global kf6_version 6.18.0

Name:       kde-kitinerary
Release:    1%{?dist}
Version:    25.08.2
License:    ASL-2.0 and BSD-3-Clause and CC0-1.0 and LGPLv2+
Summary:    Data Model and Extraction System for Travel Reservation information
Url:        https://invent.kde.org/pim/kitinerary
#Source0:    https://invent.kde.org/pim/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: kf6-extra-cmake-modules >= %kf6_version
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-qttools-devel

BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(poppler-cpp)
BuildRequires: pkgconfig(zxing)

# meeds either custom build, or sailfishos master:
#BuildRequires: poppler-private-devel

#BuildRequires: qt6-qtbase-devel
BuildRequires: pkgconfig(Qt6Core)

BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-kcontacts-devel
BuildRequires:  kf6-kcalendarcore-devel >= %kf6_version
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  kf6-kconfig-devel

BuildRequires:  kde-kmime-devel
BuildRequires:  kde-kpkpass-devel

BuildRequires:  libphonenumber-devel
BuildRequires:  pkgconfig(libxml-2.0)

%description
%{summary}.

The itinerary data extraction engine extracts travel-related information from
input in various forms, from PDF documents to ticket barcodes, from emails to
calendar events, and provides that in a machine-readable way.

%package devel
Summary:    Development files for %{name}
License:    ASL-2.0 and BSD-3-Clause and CC0-1.0 and LGPLv2+
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake_kf6 \
    -DCMAKE_DISABLE_FIND_PACKAGE_OsmTools=ON \
    -DBUILD_TESTING=OFF \
    %{nil}

%cmake_build

%install
%cmake_install

%find_lang kitinerary6

%files -f kitinerary6.lang
%{_kf6_libexecdir}/kitinerary-extractor
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_libdir}/libKPim6Itinerary.so.*
%{_kf6_datadir}/mime/packages/*xml


%files devel
%{_includedir}/KPim6/KItinerary/
%{_includedir}/KPim6/kitinerary/
%{_includedir}/KPim6/kitinerary_version.h
%{_libdir}/libKPim6Itinerary.so
%{_libdir}/cmake/KPim6Itinerary/
