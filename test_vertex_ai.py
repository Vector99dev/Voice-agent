#!/usr/bin/env python3
"""Diagnostic script to check Vertex AI setup"""

import os
import subprocess
import sys

def check_gcloud_auth():
    """Check if gcloud is authenticated"""
    try:
        result = subprocess.run(['gcloud', 'auth', 'list'], 
                              capture_output=True, text=True)
        if 'ACTIVE' in result.stdout:
            print("✅ gcloud authentication: OK")
            return True
        else:
            print("❌ gcloud authentication: FAILED")
            return False
    except Exception as e:
        print(f"❌ gcloud not installed or error: {e}")
        return False

def check_project():
    """Check if project is set"""
    try:
        result = subprocess.run(['gcloud', 'config', 'get-value', 'project'], 
                              capture_output=True, text=True)
        project = result.stdout.strip()
        if project:
            print(f"✅ Project set: {project}")
            return project
        else:
            print("❌ No project set")
            return None
    except Exception as e:
        print(f"❌ Error getting project: {e}")
        return None

def check_vertex_ai_api():
    """Check if Vertex AI API is enabled"""
    try:
        result = subprocess.run(['gcloud', 'services', 'list', '--enabled', 
                               '--filter=name:aiplatform.googleapis.com'], 
                              capture_output=True, text=True)
        if 'aiplatform.googleapis.com' in result.stdout:
            print("✅ Vertex AI API: ENABLED")
            return True
        else:
            print("❌ Vertex AI API: NOT ENABLED")
            return False
    except Exception as e:
        print(f"❌ Error checking API: {e}")
        return False

def check_region():
    """Check current region"""
    try:
        result = subprocess.run(['gcloud', 'config', 'get-value', 'compute/region'], 
                              capture_output=True, text=True)
        region = result.stdout.strip()
        if region:
            print(f"✅ Region set: {region}")
            return region
        else:
            print("❌ No region set")
            return None
    except Exception as e:
        print(f"❌ Error getting region: {e}")
        return None

def main():
    print("🔍 Vertex AI Diagnostic Check")
    print("=" * 40)
    
    # Check authentication
    auth_ok = check_gcloud_auth()
    
    # Check project
    project = check_project()
    
    # Check API
    api_ok = check_vertex_ai_api()
    
    # Check region
    region = check_region()
    
    print("\n📋 Summary:")
    print(f"Authentication: {'✅ OK' if auth_ok else '❌ FAILED'}")
    print(f"Project: {'✅ OK' if project else '❌ FAILED'}")
    print(f"Vertex AI API: {'✅ ENABLED' if api_ok else '❌ NOT ENABLED'}")
    print(f"Region: {'✅ OK' if region else '❌ FAILED'}")
    
    if not api_ok:
        print("\n🔧 To enable Vertex AI API:")
        print("gcloud services enable aiplatform.googleapis.com")
    
    if not region:
        print("\n🔧 To set region:")
        print("gcloud config set compute/region us-central1")

if __name__ == "__main__":
    main() 
