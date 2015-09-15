Name:           ros-indigo-gazebo-ros
Version:        2.4.9
Release:        1%{?dist}
Summary:        ROS gazebo_ros package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo
Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-gazebo-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rosgraph-msgs
Requires:       ros-indigo-roslib
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf
Requires:       tinyxml-devel
BuildRequires:  gazebo
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-gazebo-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rosgraph-msgs
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf
BuildRequires:  tinyxml-devel

%description
Provides ROS plugins that offer message and service publishers for interfacing
with Gazebo through ROS. Formally simulator_gazebo/gazebo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Sep 15 2015 John Hsu <hsu@osrfoundation.org> - 2.4.9-1
- Autogenerated by Bloom

* Sun Aug 16 2015 John Hsu <hsu@osrfoundation.org> - 2.4.9-0
- Autogenerated by Bloom

* Wed Aug 12 2015 John Hsu <hsu@osrfoundation.org> - 2.4.8-1
- Autogenerated by Bloom

* Tue Mar 17 2015 John Hsu <hsu@osrfoundation.org> - 2.4.8-0
- Autogenerated by Bloom

* Thu Dec 18 2014 John Hsu <hsu@osrfoundation.org> - 2.4.7-1
- Autogenerated by Bloom

* Mon Dec 15 2014 John Hsu <hsu@osrfoundation.org> - 2.4.7-0
- Autogenerated by Bloom

* Mon Sep 01 2014 John Hsu <hsu@osrfoundation.org> - 2.4.6-0
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.4.5-0
- Autogenerated by Bloom

