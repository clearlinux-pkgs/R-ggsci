#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-ggsci
Version  : 3.0.3
Release  : 2
URL      : https://cran.r-project.org/src/contrib/ggsci_3.0.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggsci_3.0.3.tar.gz
Summary  : Scientific Journal and Sci-Fi Themed Color Palettes for
Group    : Development/Tools
License  : GPL-3.0
Requires: R-ggplot2
Requires: R-scales
BuildRequires : R-ggplot2
BuildRequires : R-gridExtra
BuildRequires : R-reshape2
BuildRequires : R-scales
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
plots in scientific journals, data visualization libraries,
    science fiction movies, and TV shows.

%prep
%setup -q -n ggsci

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713890697

%install
export SOURCE_DATE_EPOCH=1713890697
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggsci/DESCRIPTION
/usr/lib64/R/library/ggsci/INDEX
/usr/lib64/R/library/ggsci/Meta/Rd.rds
/usr/lib64/R/library/ggsci/Meta/features.rds
/usr/lib64/R/library/ggsci/Meta/hsearch.rds
/usr/lib64/R/library/ggsci/Meta/links.rds
/usr/lib64/R/library/ggsci/Meta/nsInfo.rds
/usr/lib64/R/library/ggsci/Meta/package.rds
/usr/lib64/R/library/ggsci/Meta/vignette.rds
/usr/lib64/R/library/ggsci/NAMESPACE
/usr/lib64/R/library/ggsci/NEWS.md
/usr/lib64/R/library/ggsci/R/ggsci
/usr/lib64/R/library/ggsci/R/ggsci.rdb
/usr/lib64/R/library/ggsci/R/ggsci.rdx
/usr/lib64/R/library/ggsci/R/sysdata.rdb
/usr/lib64/R/library/ggsci/R/sysdata.rdx
/usr/lib64/R/library/ggsci/doc/ggsci-faq.R
/usr/lib64/R/library/ggsci/doc/ggsci-faq.Rmd
/usr/lib64/R/library/ggsci/doc/ggsci-faq.html
/usr/lib64/R/library/ggsci/doc/ggsci.R
/usr/lib64/R/library/ggsci/doc/ggsci.Rmd
/usr/lib64/R/library/ggsci/doc/ggsci.html
/usr/lib64/R/library/ggsci/doc/index.html
/usr/lib64/R/library/ggsci/help/AnIndex
/usr/lib64/R/library/ggsci/help/aliases.rds
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-aaas-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-cosmic-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-cosmic-2.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-cosmic-3.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-d3-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-flatui-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-frontiers-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-futurama-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-gsea-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-igv-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-jama-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-jco-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-lancet-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-locuszoom-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-material-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-nejm-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-npg-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-rickandmorty-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-simpsons-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-startrek-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-tron-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-uchicago-1.png
/usr/lib64/R/library/ggsci/help/figures/README-ggsci-ucscgb-1.png
/usr/lib64/R/library/ggsci/help/figures/logo.png
/usr/lib64/R/library/ggsci/help/ggsci.rdb
/usr/lib64/R/library/ggsci/help/ggsci.rdx
/usr/lib64/R/library/ggsci/help/paths.rds
/usr/lib64/R/library/ggsci/html/00Index.html
/usr/lib64/R/library/ggsci/html/R.css
/usr/lib64/R/library/ggsci/logo/logo.R
