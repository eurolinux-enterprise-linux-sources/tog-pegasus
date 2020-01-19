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
/* NOCHKSRC */

//
//%/////////////////////////////////////////////////////////////////////////////

#ifndef Pegasus_Exception_h
#define Pegasus_Exception_h

#include <Pegasus/Common/Config.h>
#include <Pegasus/Common/String.h>
#include <Pegasus/Common/CIMStatusCode.h>
#include <Pegasus/Common/MessageLoader.h>  // l10n
#include <Pegasus/Common/Linkage.h>
#include <Pegasus/Common/ContentLanguages.h>  // l10n

PEGASUS_NAMESPACE_BEGIN
class ExceptionRep;

/** 
<p>The <tt>Exception</tt> class is the parent class for all
exceptions that can be generated by any component of the
Pegasus infrastructure. It includes not only the CIM exceptions
that are defined by the DMTF, but also various exceptions that
may occur during the processing of functions called by clients
and providers.</p>
*/
class PEGASUS_COMMON_LINKAGE Exception
{
public:

    ///
    Exception(const String& message);

    ///
    Exception(const Exception& exception);

// l10n
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    Exception(const MessageLoaderParms& msgParms);
#endif

    ///
    virtual ~Exception();

    ///
    virtual const String& getMessage() const;
    
// l10n
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    // Note: Rlse 2.3 - not virtual to preserve binary compatibility.
    /** <I><B>Experimental Interface</B></I><BR>
    */
    const ContentLanguages& getContentLanguages() const;
    
    // Note: Rlse 2.3 - not virtual to preserve binary compatibility.
    /** <I><B>Experimental Interface</B></I><BR>
    */
    void setContentLanguages(const ContentLanguages& langs); 
#endif   

protected:

    Exception();

    ExceptionRep * _rep;
};

///
class PEGASUS_COMMON_LINKAGE IndexOutOfBoundsException : public Exception
{
public:
    ///
    IndexOutOfBoundsException();
};

///
class PEGASUS_COMMON_LINKAGE AlreadyExistsException : public Exception
{
public:
    ///
    AlreadyExistsException(const String& message);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    AlreadyExistsException(MessageLoaderParms& msgParms);
#endif
};

///
class PEGASUS_COMMON_LINKAGE InvalidNameException : public Exception
{
public:
    ///
    InvalidNameException(const String& name);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    InvalidNameException(MessageLoaderParms& msgParms); 
#endif   
};

///
class PEGASUS_COMMON_LINKAGE InvalidNamespaceNameException : public Exception
{
public:
    ///
    InvalidNamespaceNameException(const String& name);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    InvalidNamespaceNameException(MessageLoaderParms& msgParms);
#endif    
};

///
class PEGASUS_COMMON_LINKAGE UninitializedObjectException : public Exception
{
public:
    ///
    UninitializedObjectException();
};

///
class PEGASUS_COMMON_LINKAGE TypeMismatchException : public Exception
{
public:
    ///
    TypeMismatchException();
    TypeMismatchException(const String& message);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    TypeMismatchException(MessageLoaderParms& msgParms);
#endif    

};

///
class PEGASUS_COMMON_LINKAGE DynamicCastFailedException : public Exception
{
public:
    ///
    DynamicCastFailedException();
};

///
class PEGASUS_COMMON_LINKAGE InvalidDateTimeFormatException : public Exception
{
public:
    ///
    InvalidDateTimeFormatException();
};

///
class PEGASUS_COMMON_LINKAGE MalformedObjectNameException : public Exception
{
public:
    ///
    MalformedObjectNameException(const String& objectName);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    MalformedObjectNameException(MessageLoaderParms& msgParms); 
#endif   
};

///
class PEGASUS_COMMON_LINKAGE BindFailedException : public Exception
{
public:
    ///
    BindFailedException(const String& message);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    BindFailedException(MessageLoaderParms& msgParms);
#endif    
};

///
class PEGASUS_COMMON_LINKAGE InvalidLocatorException : public Exception
{
public:
    ///
    InvalidLocatorException(const String& locator);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    InvalidLocatorException(MessageLoaderParms& msgParms); 
#endif  
};

///
class PEGASUS_COMMON_LINKAGE CannotCreateSocketException : public Exception
{
public:
    ///
    CannotCreateSocketException();
};

///
class PEGASUS_COMMON_LINKAGE CannotConnectException : public Exception
{
public:
    ///
    CannotConnectException(const String& message);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    CannotConnectException(MessageLoaderParms& msgParms); 
#endif  
};

///
class PEGASUS_COMMON_LINKAGE AlreadyConnectedException: public Exception
{
public:
    ///
    AlreadyConnectedException();
};

///
class PEGASUS_COMMON_LINKAGE NotConnectedException: public Exception
{
public:
    ///
    NotConnectedException();
};

///
class PEGASUS_COMMON_LINKAGE ConnectionTimeoutException: public Exception
{
public:
    ///
    ConnectionTimeoutException();
};

///
class PEGASUS_COMMON_LINKAGE SSLException: public Exception
{
public:
    ///
    SSLException(const String& message);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    SSLException(MessageLoaderParms& msgParms); 
#endif   
};

///
class PEGASUS_COMMON_LINKAGE DateTimeOutOfRangeException : public Exception
{
public:
    ///
    DateTimeOutOfRangeException(const String& message);
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    DateTimeOutOfRangeException(MessageLoaderParms& msgParms);
#endif     
}; 

/** The CIMException defines the CIM exceptions that are formally defined in
    the CIM Operations over HTTP specification.
*/
class PEGASUS_COMMON_LINKAGE CIMException : public Exception
{
public:

    ///
    CIMException(
	CIMStatusCode code = CIM_ERR_SUCCESS,
	const String& message = String::EMPTY);
	
// l10n	
#ifdef PEGASUS_USE_EXPERIMENTAL_INTERFACES
    /** <I><B>Experimental Interface</B></I><BR>
    */
    CIMException(
	CIMStatusCode code,
	const MessageLoaderParms& msgParms);
#endif	

    ///
    CIMException(const CIMException & cimException);

    ///
    CIMException& operator=(const CIMException & cimException);

    ///
    virtual ~CIMException();

    ///
    CIMStatusCode getCode() const;
};


PEGASUS_NAMESPACE_END

#endif /* Pegasus_Exception_h */
