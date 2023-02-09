# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: sonobuoy
Epoch: 100
Version: 0.56.13
Release: 1%{?dist}
Summary: Conformance test suite for diagnosing a Kubernetes cluster
License: Apache-2.0
URL: https://github.com/vmware-tanzu/sonobuoy/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: golang-1.20
BuildRequires: glibc-static

%description
Sonobuoy is a diagnostic tool for understanding the state of a
Kubernetes cluster by running a set of Kubernetes conformance tests in
an accessible and non-destructive manner.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
mkdir -p bin
set -ex && \
    export CGO_ENABLED=0 && \
    go build \
        -mod vendor -buildmode pie -v \
        -ldflags "-s -w -extldflags '-static -lm'" \
        -o ./bin/sonobuoy .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -t %{buildroot}%{_bindir}/ bin/sonobuoy

%files
%license LICENSE
%{_bindir}/*

%changelog
