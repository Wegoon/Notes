/*************************************************************************************
 * Copyright 2012 NEU NLP Lab. All rights reserved.
 * File Name: readfile.h
 * Author: Bai Longfei
 * Email: s-kira@live.cn
 * Time: 2012.08.16
 * Create for MT-PreProcessing Engine
 *************************************************************************************/

#ifndef __READFILE_H__
#define __READFILE_H__

#include <string>
using std::string;
using std::wstring;

#ifdef linux
#include <cstdlib>
#include <locale>
#else
#include <Windows.h>
#endif

#include <cstdio>
#include <cstring>

class CReadFile {
   public:
    FILE* mp_fileHandle;
    bool m_isUTF8;
    bool m_isOutput;
    bool m_isEnd;
    unsigned int m_lineNum;
    char* mp_fileName;
    unsigned int m_num;
    CReadFile(const char* path, bool isUTF8 = true, bool isOutput = false,
              unsigned int num = 1000) {
        mp_fileHandle = nullptr;
        open(path, isUTF8, isOutput, num);
    }

    ~CReadFile() {
        if (mp_fileHandle) {
            close();
            mp_fileHandle = nullptr;
        }
    }

    void open(const char* path, bool isUTF8 = true, bool isOutput = false,
              unsigned int num = 1000) {
        if (mp_fileHandle) close();

        mp_fileName = new char[strlen(path) + 1];
        strcpy(mp_fileName, path);
        mp_fileHandle = fopen(path, "rb");
        m_isEnd = isFileNotOpen();
        m_isUTF8 = isUTF8;
        m_isOutput = isOutput;
        m_lineNum = 0;
        m_num = num;
    }

    void close() {
        if (mp_fileHandle) {
            fclose(mp_fileHandle);
            mp_fileHandle = nullptr;
            m_isEnd = true;
            m_lineNum = 0;
            delete[] mp_fileName;
        }
    }

    bool isFileNotOpen() { return mp_fileHandle == nullptr; }

    bool isEnd() { return m_isEnd; }

    bool ReadLineStr(string& line) {
        char* pline = read();
        if (pline != nullptr) {
            line = pline;
            delete[] pline;

            trim(line);

            if (++m_lineNum % m_num == 0 && m_isOutput)
                fprintf(stdout, "\r%s : already read %u lines.", mp_fileName,
                        m_lineNum);

            return true;
        } else {
            if (m_isOutput)
                fprintf(stdout, "\r%s : already read %u lines.\n", mp_fileName,
                        m_lineNum);
            return false;
        }
    }

    bool ReadLine(wstring& line) {
        char* pline = read();
        if (pline != nullptr) {
            if (m_isUTF8)
                line = UTF8ToUnicode(pline);
            else
                line = GBToUnicode(pline);

            delete[] pline;

            trim(line);

            if (++m_lineNum % 1000 == 0 && m_isOutput)
                fprintf(stdout, "\r%s : already read %u lines.", mp_fileName,
                        m_lineNum);

            return true;
        } else {
            if (m_isOutput)
                fprintf(stdout, "\r%s : already read %u lines.\n", mp_fileName,
                        m_lineNum);
            return false;
        }
    }

    char* read() {
        unsigned long ullLineLen = 128;
        char* p_szLine = new char[ullLineLen];
        if (!fgets(p_szLine, (int)ullLineLen, mp_fileHandle)) {
            if (feof(mp_fileHandle)) {
            } else if (ferror(mp_fileHandle)) {
                fprintf(stderr, "reading file failed!");
            }
            delete[] p_szLine;
            m_isEnd = true;
            return nullptr;
        }
        /* read the rest part of line into string buffer */
        while (p_szLine[strlen(p_szLine) - 1] != '\n') {
            char* p_szTmpPtr = NULL;
            unsigned long ullTmpLen = ullLineLen + 1;
            char* p_szOldLine = p_szLine;
            ullLineLen *= 2;
            p_szLine = new char[ullLineLen];
            strcpy(p_szLine, p_szOldLine);
            delete[] p_szOldLine;
            p_szTmpPtr = p_szLine + strlen(p_szLine);
            if (!fgets(p_szTmpPtr, (int)ullTmpLen, mp_fileHandle)) {
                if (feof(mp_fileHandle)) {
                    break;
                } else {
                    fprintf(stderr, "reading file failed!");
                    delete[] p_szLine;
                    m_isEnd = true;
                    return nullptr;
                }
            }
        }

        if (p_szLine == nullptr) {
            m_isEnd = true;
            return nullptr;
        }

        return p_szLine;
    }

    static void trim(wstring& str) {
        wstring::size_type pos = 0;
        while ((pos = str.find(L'\r')) != wstring::npos) str.erase(pos, 1);
        while ((pos = str.find(L'\n')) != wstring::npos) str.erase(pos, 1);
    }

    static void trim(string& str) {
        string::size_type pos = 0;
        while ((pos = str.find('\r')) != string::npos) str.erase(pos, 1);
        while ((pos = str.find('\n')) != string::npos) str.erase(pos, 1);
    }

    static wstring UTF8ToUnicode(const char* line) {
#ifdef linux
        setlocale(LC_ALL, "zh_CN.UTF-8");
        size_t size = mbstowcs(NULL, line, 0);
        wchar_t* wcstr = new wchar_t[size + 1];
        if (!wcstr) return L"";
        mbstowcs(wcstr, line, size + 1);
#else
        size_t size = MultiByteToWideChar(CP_UTF8, 0, line, -1, NULL, 0);
        wchar_t* wcstr = new wchar_t[size];
        if (!wcstr) return L"";
        MultiByteToWideChar(CP_UTF8, 0, line, -1, wcstr, size);
#endif
        wstring final(wcstr);
        delete[] wcstr;

        return final;
    }

    static wstring GBToUnicode(const char* line) {
#ifdef linux
        setlocale(LC_ALL, "zh_CN.GB2312");
        size_t size = mbstowcs(NULL, line, 0);
        wchar_t* wcstr = new wchar_t[size + 1];
        if (!wcstr) return L"";
        mbstowcs(wcstr, line, size + 1);
#else
        size_t size = MultiByteToWideChar(CP_ACP, 0, line, -1, NULL, 0);
        wchar_t* wcstr = new wchar_t[size];
        if (!wcstr) return L"";
        MultiByteToWideChar(CP_ACP, 0, line, -1, wcstr, size);
#endif
        wstring final(wcstr);
        delete[] wcstr;

        return final;
    }
};

#endif