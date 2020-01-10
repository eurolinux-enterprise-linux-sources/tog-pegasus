//%LICENSE////////////////////////////////////////////////////////////////
//
// Licensed to The Open Group (TOG) under one or more contributor license
// agreements.  Refer to the OpenPegasusNOTICE.txt file distributed with
// this work for additional information regarding copyright ownership.
// Each contributor licenses this file to you under the OpenPegasus Open
// Source License; you may not use this file except in compliance with the
// License.
//
// Permission is hereby granted, free of charge, to any person obtaining a
// copy of this software and associated documentation files (the "Software"),
// to deal in the Software without restriction, including without limitation
// the rights to use, copy, modify, merge, publish, distribute, sublicense,
// and/or sell copies of the Software, and to permit persons to whom the
// Software is furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included
// in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
// OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
// IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
// CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
// TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
// SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
//
//////////////////////////////////////////////////////////////////////////
//
//%/////////////////////////////////////////////////////////////////////////////

#include <Pegasus/Common/PegasusAssert.h>
#include <cstdlib>
#include <iostream>
#include <Pegasus/Common/HostAddress.h>

PEGASUS_USING_PEGASUS;
PEGASUS_USING_STD;

void testHostAddress()
{
    // Check for valid hostnames or addresses
    HostAddress hostaddr("1.222.33.44");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() == String("1.222.33.44"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_IPV4);

    hostaddr.setHostAddress("1.2.3.4");
    HostAddress hostaddr2(hostaddr);
    PEGASUS_TEST_ASSERT(hostaddr2.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr2.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV4Address(hostaddr2.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr2.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr2.getHost() == String("1.2.3.4"));
    PEGASUS_TEST_ASSERT(hostaddr2.getAddressType() == HostAddress::AT_IPV4);


    hostaddr.setHostAddress("fe00:ef::1");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() == String("fe00:ef::1"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_IPV6);


    hostaddr.setHostAddress("fe00:1::");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() == String("fe00:1::"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_IPV6);

    hostaddr.setHostAddress("::1");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() == String("::1"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_IPV6);

    hostaddr.setHostAddress("fe00:1231:23fe:3456:acde:ebcd:12fe:ecd4");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() ==
        String("fe00:1231:23fe:3456:acde:ebcd:12fe:ecd4"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_IPV6);

    hostaddr.setHostAddress("fe00:1231:23fe:3456::ebcd:12fe:ecd4");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() ==
        String("fe00:1231:23fe:3456::ebcd:12fe:ecd4"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_IPV6);

    hostaddr.setHostAddress("123.34.abcd.xyz.com");
    PEGASUS_TEST_ASSERT(hostaddr.isValid());
    PEGASUS_TEST_ASSERT(HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr.getHost() == String("123.34.abcd.xyz.com"));
    PEGASUS_TEST_ASSERT(hostaddr.getAddressType() == HostAddress::AT_HOSTNAME);


    // Invalid hostnames or addresses

    HostAddress hostaddr3;
    PEGASUS_TEST_ASSERT(hostaddr3.getHost() == String::EMPTY);

    hostaddr.setHostAddress("[1.2.3.4]:");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(hostaddr3.getHost() == String::EMPTY);

    hostaddr.setHostAddress("[1.2.3.4]:1234");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[1.2.3.4]");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    // must not be enclosed in brackets.
    hostaddr.setHostAddress("[fe00:ef::1]");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[ffff1:2:3:4]");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[123]:123345");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[]");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[::1]");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[1::24]:");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("[xyz.com]");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));

    hostaddr.setHostAddress("xyz.com:123241");
    PEGASUS_TEST_ASSERT(!hostaddr.isValid());
    PEGASUS_TEST_ASSERT(!HostAddress::isValidHostName(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV4Address(hostaddr.getHost()));
    PEGASUS_TEST_ASSERT(!HostAddress::isValidIPV6Address(hostaddr.getHost()));
}

int main(int argc, char** argv)
{
    testHostAddress();
    cout << argv[0] << " +++++ passed all tests" << endl;

    return 0;
}
