%define name    mailscanner

# Hey you, who are looking this spec
# welcome in hell !
# This software just sucks !

%define sourcename MailScanner
%define ver 4.64.3
%define rel 2
%define srcversion %{ver}-%{rel}
%define version %{ver}_%{rel}
%define release %mkrel 1

%define _provides_exceptions perl(MIME::Entity)

Name:        %{name}
Version:     %{version}
Release:     %{release}
Summary:     E-Mail Gateway Virus Scanner and Spam Detector
Group:       Networking/Mail
License:   GPL
URL:         http://www.mailscanner.info/
Source:      %{sourcename}-%{srcversion}.tar.gz
Source1:	MailScanner.conf
Source2: cron.daily_clean.quarantine
Source3: cron.daily_update_phishing_sites
Source4: cron.daily_update_spamassassin
Source5: cron.hourly_check_MailScanner
Source6: cron.hourly_update_bad_phishing_sites
Source7: cron.hourly_update_virus_scanners
Source8: MailScanner.init
Source9: MailScanner.opt
BuildRoot:   %{_tmppath}/%{name}-root
BuildArch: noarch
# This file is provided, but the inernal package named differ :\
# This app really sucks !
Provides: perl(MailScanner::MCPMessage)
BuildRequires: perl(Mail::SpamAssassin)

%description
MailScanner is a freely distributable E-Mail gateway virus scanner and
spam detector. It uses Postfix, sendmail, ZMailer, Qmail or Exim as its basis,
and a choice of 22 commercial virus scanning engines to do the actual
virus scanning.  It can decode and scan attachments intended solely
for Microsoft Outlook users (MS-TNEF). If possible, it will disinfect
infected documents and deliver them automatically. It provides protection
against many security vulnerabilities in widely-used e-mail programs
such as Eudora and Microsoft Outlook. It will also selectively filter
the content of email messages to protect users from offensive content
such as pornographic spam. It also has features which protect it against
Denial Of Service attacks.

After installation, you must install one of the supported commercial anti-
virus packages.

%package spamassassin
Group: Networking/Mail
Summary: Mailscanner spamassassin part
Requires: perl(Mail::SpamAssassin)

%description spamassassin
This package provide the proper mailscanner configuration to run
spamassassin rules.


%prep
%setup -q -n %{sourcename}-%{srcversion}
# Install custom config file
cat %{SOURCE1} > etc/MailScanner.conf

%install
perl -pi - bin/MailScanner/ConfigDefs.pl etc/MailScanner.conf etc/virus.scanners.conf bin/mailscanner bin/Sophos.install bin/update_virus_scanners bin/update_phishing_sites <<EOF
s+/opt/MailScanner/etc/mailscanner.conf+/etc/MailScanner/MailScanner.conf+;
s+/opt/MailScanner/etc/virus.scanners.conf+/etc/MailScanner/virus.scanners.conf+;
s./opt/MailScanner/var./var/run.;
s./opt/MailScanner/bin/tnef./usr/bin/tnef.;
s./opt/MailScanner/etc/reports./etc/MailScanner/reports.;
s./opt/MailScanner/etc/rules./etc/MailScanner/rules.;
s./opt/MailScanner/etc./etc/MailScanner.;
s./opt/MailScanner/lib./usr/lib/MailScanner.;
s./opt/MailScanner/bin./usr/lib/MailScanner.;
s./usr/lib/sendmail./usr/sbin/sendmail.;
EOF
perl -pi - check_MailScanner <<EOF
s+/opt/MailScanner/etc/mailscanner.conf+/etc/MailScanner/MailScanner.conf+;
s./opt/MailScanner/var./var/run.;
s./opt/MailScanner/bin/tnef./usr/bin/tnef.;
s./opt/MailScanner/etc/reports./etc/MailScanner/reports.;
s./opt/MailScanner/etc/rules./etc/MailScanner/rules.;
s./opt/MailScanner/etc/mcp./etc/MailScanner/mcp.;
s./opt/MailScanner/etc./etc/MailScanner.;
s./opt/MailScanner/lib./usr/lib/MailScanner.;
s./opt/MailScanner/bin./usr/sbin.;
s./usr/lib/sendmail./usr/sbin/sendmail.;
EOF

mkdir -p $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rc.d/init.d
mkdir -p ${RPM_BUILD_ROOT}%_sbindir
mkdir -p ${RPM_BUILD_ROOT}%_mandir/man8
mkdir -p ${RPM_BUILD_ROOT}%_mandir/man5
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/cy+en
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/de
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/en
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/fr
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/es
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/nl
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/pt_br
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/dk
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/sk
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/it
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/ro
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/se
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/cz
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/hu
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/reports/ca
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/rules
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/MailScanner/mcp
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/MailScanner/
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/MailScanner/MailScanner
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/MailScanner/MailScanner/CustomFunctions
mkdir -p ${RPM_BUILD_ROOT}/usr/share/MailScanner/
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.hourly
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/cron.daily
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
mkdir -p ${RPM_BUILD_ROOT}/var/spool/mqueue.in
#mkdir -p ${RPM_BUILD_ROOT}/var/spool/MailScanner/incoming
#mkdir -p ${RPM_BUILD_ROOT}/var/spool/MailScanner/quarantine
mkdir -p ${RPM_BUILD_ROOT}/var/run

install bin/df2mbox            ${RPM_BUILD_ROOT}%_sbindir/df2mbox
install bin/d2mbox             ${RPM_BUILD_ROOT}%_sbindir/d2mbox
install bin/MailScanner        ${RPM_BUILD_ROOT}%_sbindir/MailScanner
install bin/check_mailscanner      ${RPM_BUILD_ROOT}%_sbindir/check_MailScanner
(
cd ${RPM_BUILD_ROOT}%{_sbindir}
rm -f check_mailscanner
ln -s check_MailScanner check_mailscanner
)

install bin/Sophos.install     ${RPM_BUILD_ROOT}%{_sbindir}/Sophos.install
install bin/update_virus_scanners ${RPM_BUILD_ROOT}%{_sbindir}/update_virus_scanners
install bin/update_phishing_sites ${RPM_BUILD_ROOT}%{_sbindir}/update_phishing_sites
install bin/analyse_SpamAssassin_cache ${RPM_BUILD_ROOT}%{_sbindir}/analyse_SpamAssassin_cache
ln -sf analyse_SpamAssassin_cache ${RPM_BUILD_ROOT}%{_sbindir}/analyze_SpamAssassin_cache
install bin/upgrade_MailScanner_conf ${RPM_BUILD_ROOT}%{_sbindir}/upgrade_MailScanner_conf
ln -sf upgrade_MailScanner_conf ${RPM_BUILD_ROOT}%{_sbindir}/upgrade_languages_conf
#install doc/MailScanner.8   ${RPM_BUILD_ROOT}%{_mandir}/man8/
#install doc/MailScanner.conf.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/

while read f 
do
  install etc/$f ${RPM_BUILD_ROOT}/%_sysconfdir/MailScanner/
done << EOF
filename.rules.conf
filetype.rules.conf
MailScanner.conf
spam.assassin.prefs.conf
spam.lists.conf
virus.scanners.conf
phishing.safe.sites.conf
country.domains.conf
EOF

while read f
do
  install etc/mcp/$f ${RPM_BUILD_ROOT}/%_sysconfdir/MailScanner/mcp/
done << EOF2
10_example.cf
mcp.spam.assassin.prefs.conf
EOF2


for lang in en cy+en de fr es nl pt_br sk dk it ro se cz hu ca
do
  while read f 
  do
    install etc/reports/$lang/$f ${RPM_BUILD_ROOT}%_sysconfdir/MailScanner/reports/$lang
  done << EOF
deleted.content.message.txt
deleted.filename.message.txt
deleted.virus.message.txt
disinfected.report.txt
inline.sig.html
inline.sig.txt
inline.spam.warning.txt
inline.warning.html
inline.warning.txt
languages.conf
recipient.spam.report.txt
recipient.mcp.report.txt
rejection.report.txt
sender.content.report.txt
sender.error.report.txt
sender.filename.report.txt
sender.spam.rbl.report.txt
sender.spam.report.txt
sender.spam.sa.report.txt
sender.mcp.report.txt
sender.virus.report.txt
stored.content.message.txt
stored.filename.message.txt
stored.virus.message.txt
EOF
done

install etc/reports/de/README.1ST ${RPM_BUILD_ROOT}%_sysconfdir/MailScanner/reports/de
install etc/reports/se/README     ${RPM_BUILD_ROOT}%_sysconfdir/MailScanner/reports/se

while read f 
do
  install etc/rules/$f ${RPM_BUILD_ROOT}%_sysconfdir/MailScanner/rules
done << EOF
EXAMPLES
README
spam.whitelist.rules
bounce.rules
max.message.size.rules
EOF

while read f 
do
  install lib/$f ${RPM_BUILD_ROOT}/usr/lib/MailScanner
done << EOF
antivir-autoupdate
antivir-wrapper
avg-autoupdate
avg-wrapper
bitdefender-wrapper
bitdefender-autoupdate
clamav-autoupdate
clamav-wrapper
css-autoupdate
css-wrapper
command-wrapper
drweb-wrapper
f-prot-autoupdate
f-prot-wrapper
f-secure-wrapper
f-secure-autoupdate
etrust-autoupdate
etrust-wrapper
generic-autoupdate
generic-wrapper
inoculan-autoupdate
inoculan-wrapper
inoculate-wrapper
kaspersky.prf
kaspersky-autoupdate
kaspersky-wrapper
kavdaemonclient-wrapper
mcafee-autoupdate
mcafee-wrapper
nod32-wrapper
nod32-autoupdate
norman-wrapper
norman-autoupdate
panda-wrapper
panda-autoupdate
rav-autoupdate
rav-wrapper
sophos-autoupdate
sophos-wrapper
symscanengine-autoupdate
symscanengine-wrapper
trend-autoupdate
trend-wrapper
vexira-autoupdate
vexira-wrapper
EOF

install %{SOURCE2} %buildroot%_sysconfdir/cron.daily/clean.quarantine
install %{SOURCE3} %buildroot%_sysconfdir/cron.daily/update_phishing_sites
install %{SOURCE4} %buildroot%_sysconfdir/cron.daily/update_spamassassin
install %{SOURCE5} %buildroot%_sysconfdir/cron.hourly/check_MailScanner
install %{SOURCE6} %buildroot%_sysconfdir/cron.hourly/update_bad_phishing_sites
install %{SOURCE7} %buildroot%_sysconfdir/cron.hourly/update_virus_scanners

install %{SOURCE8} %buildroot%_sysconfdir/rc.d/init.d/MailScanner
install %{SOURCE9} %buildroot%_sysconfdir/sysconfig/MailScanner

# Lib installation
(cd lib; tar cf - .) | (cd ${RPM_BUILD_ROOT}/usr/lib/MailScanner/; tar xvf -)

install var/MailScanner.pid ${RPM_BUILD_ROOT}/var/run/

(
cd %buildroot/%_sysconfdir/MailScanner/
SADIR=`perl -MMail::SpamAssassin -e 'print Mail::SpamAssassin->new->first_existing_path(@Mail::SpamAssassin::site_rules_path)'`
ln -s spam.assassin.prefs.conf ${SADIR}/mailscanner.cf
)

cat >README.urpmi<<EOF
To activate MailScanner run the following commands:

For postfix:
   service postfix stop
   chkconfig --del postfix
For sendmail:
   service sendmail stop
   chkconfig --del sendmail

And:
   chkconfig --add MailScanner
   service MailScanner start

For technical support, please read the MAQ at www.mailscanner.biz/maq/
and buy the book at www.mailscanner.info/store
EOF

%clean
rm -rf ${RPM_BUILD_ROOT}

%post

#Configure postfix via postconf
postconf -e "header_checks = regexp:/etc/postfix/header_checks"
echo "/^Received:/ HOLD" >> /etc/postfix/header_checks

# Create the incoming and quarantine dirs if needed
for F in incoming quarantine
do
  if [ \! -d /var/spool/MailScanner/$F ]; then
    mkdir -p /var/spool/MailScanner/$F
    chown postfix.postfix /var/spool/MailScanner/$F
    chmod 0700 /var/spool/MailScanner/$F
  fi
done
# Sort out the rc.d directories
# chkconfig --add MailScanner
[ ! -d /etc/rc.d/init/sendmail ] || chkconfig --level 2 sendmail off # To fix bug in some RedHat dist's

exit 0

%preun
if [ $1 = 0 ]; then
    # We are being deleted, not upgraded
    service MailScanner stop >/dev/null 2>&1
    chkconfig MailScanner off
    chkconfig --del MailScanner
fi
exit 0

%postun
if [ "$1" -ge "1" ]; then
    # We are being upgraded or replaced, not deleted
    echo 'To upgrade your MailScanner.conf and languages.conf files automatically, run'
    echo '    upgrade_MailScanner_conf'
    echo '    upgrade_languages_conf'
    #service MailScanner restart </dev/null >/dev/null 2>&1
fi
exit 0

%files
%defattr (644,root,root)
%doc README.urpmi
%attr(700,root,root) %dir /var/spool/mqueue.in
#%attr(700,root,root) %dir /var/spool/MailScanner/incoming
#%attr(700,root,root) %dir /var/spool/MailScanner/quarantine
%attr(700,root,root) /var/run/MailScanner.pid
%attr(755,root,root) %{_sbindir}/df2mbox
%attr(755,root,root) %{_sbindir}/d2mbox
%attr(755,root,root) %{_sbindir}/MailScanner
%attr(755,root,root) %{_sbindir}/check_MailScanner
%attr(755,root,root) %{_sbindir}/check_mailscanner
%attr(755,root,root) %{_sbindir}/Sophos.install
%attr(755,root,root) %{_sbindir}/update_virus_scanners
%attr(755,root,root) %{_sbindir}/update_phishing_sites
%attr(755,root,root) %{_sbindir}/analyse_SpamAssassin_cache
%attr(755,root,root) %{_sbindir}/analyze_SpamAssassin_cache
%attr(755,root,root) %{_sbindir}/upgrade_MailScanner_conf
%attr(755,root,root) %{_sbindir}/upgrade_languages_conf
%config(noreplace) %attr(755,root,root) /%{_sysconfdir}/rc.d/init.d/MailScanner
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/cron.*/*
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/sysconfig/MailScanner

%config(noreplace) %{_sysconfdir}/MailScanner/filename.rules.conf
%config(noreplace) %{_sysconfdir}/MailScanner/filetype.rules.conf
%config(noreplace) %{_sysconfdir}/MailScanner/MailScanner.conf
%config(noreplace) %{_sysconfdir}/MailScanner/spam.assassin.prefs.conf
%config(noreplace) %{_sysconfdir}/MailScanner/spam.lists.conf
%config(noreplace) %{_sysconfdir}/MailScanner/virus.scanners.conf
%config(noreplace) %{_sysconfdir}/MailScanner/phishing.safe.sites.conf
%config(noreplace) %{_sysconfdir}/MailScanner/country.domains.conf

%config(noreplace) %{_sysconfdir}/MailScanner/mcp/10_example.cf
%config(noreplace) %{_sysconfdir}/MailScanner/mcp/mcp.spam.assassin.prefs.conf

%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/en/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cy+en/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/README.1ST
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/de/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/fr/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/es/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/nl/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/pt_br/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/sk/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/dk/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/it/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ro/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/README
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/se/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/cz/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/hu/stored.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/deleted.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/stored.content.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.content.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/deleted.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/deleted.virus.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/disinfected.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/inline.sig.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/inline.sig.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/inline.spam.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/inline.warning.html
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/inline.warning.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/languages.conf
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/recipient.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/recipient.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/rejection.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.error.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.filename.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.spam.rbl.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.spam.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.spam.sa.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.mcp.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/sender.virus.report.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/stored.filename.message.txt
%config(noreplace) %{_sysconfdir}/MailScanner/reports/ca/stored.virus.message.txt

%{_sysconfdir}/MailScanner/rules/EXAMPLES
%{_sysconfdir}/MailScanner/rules/README
%config(noreplace) %{_sysconfdir}/MailScanner/rules/spam.whitelist.rules
%config(noreplace) %{_sysconfdir}/MailScanner/rules/max.message.size.rules
%config(noreplace) %{_sysconfdir}/MailScanner/rules/bounce.rules

%attr(755,root,root) %config(noreplace) /usr/lib/MailScanner/*-autoupdate
%attr(755,root,root) %config(noreplace) /usr/lib/MailScanner/*-wrapper
/usr/lib/MailScanner/kaspersky.prf
/usr/lib/MailScanner/mcafee-autoupdate.old

/usr/lib/MailScanner/MailScanner.pm

/usr/lib/MailScanner/MailScanner/BinHex.pm
/usr/lib/MailScanner/MailScanner/ConfigDefs.pl
/usr/lib/MailScanner/MailScanner/Config.pm
%config(noreplace) /usr/lib/MailScanner/MailScanner/CustomConfig.pm
%config(noreplace) /usr/lib/MailScanner/MailScanner/CustomFunctions/*.pm
/usr/lib/MailScanner/MailScanner/Exim.pm
/usr/lib/MailScanner/MailScanner/EximDiskStore.pm
/usr/lib/MailScanner/MailScanner/GenericSpam.pm
/usr/lib/MailScanner/MailScanner/Lock.pm
/usr/lib/MailScanner/MailScanner/Log.pm
/usr/lib/MailScanner/MailScanner/Mail.pm
/usr/lib/MailScanner/MailScanner/MessageBatch.pm
/usr/lib/MailScanner/MailScanner/Message.pm
/usr/lib/MailScanner/MailScanner/PFDiskStore.pm
/usr/lib/MailScanner/MailScanner/Postfix.pm
/usr/lib/MailScanner/MailScanner/Qmail.pm
/usr/lib/MailScanner/MailScanner/QMDiskStore.pm
/usr/lib/MailScanner/MailScanner/Quarantine.pm
/usr/lib/MailScanner/MailScanner/Queue.pm
/usr/lib/MailScanner/MailScanner/RBLs.pm
/usr/lib/MailScanner/MailScanner/SA.pm
/usr/lib/MailScanner/MailScanner/Sendmail.pm
/usr/lib/MailScanner/MailScanner/SMDiskStore.pm
/usr/lib/MailScanner/MailScanner/SweepContent.pm
/usr/lib/MailScanner/MailScanner/SweepOther.pm
/usr/lib/MailScanner/MailScanner/SweepViruses.pm
/usr/lib/MailScanner/MailScanner/SystemDefs.pm
/usr/lib/MailScanner/MailScanner/MCP.pm
/usr/lib/MailScanner/MailScanner/MCPMessage.pm
/usr/lib/MailScanner/MailScanner/TNEF.pm
/usr/lib/MailScanner/MailScanner/WorkArea.pm
/usr/lib/MailScanner/MailScanner/ZMailer.pm
/usr/lib/MailScanner/MailScanner/ZMDiskStore.pm
/usr/lib/MailScanner/MailScanner/notes.txt

%files spamassassin
%defattr(-,root, root)
%_sysconfdir/MailScanner/spam.assassin.prefs.conf

