#!/bin/bash
APKTOOL_YML="apktool.yml"

if [ ! -f "$APKTOOL_YML" ]; then
    echo "Error: $APKTOOL_YML not found!"
    exit 1
fi

# Extract current versionCode (handling potential whitespace)
CURRENT_CODE=$(grep "versionCode:" $APKTOOL_YML | awk '{print $2}' | tr -d "'"")
if [ -z "$CURRENT_CODE" ]; then
    echo "Error: Could not find versionCode in $APKTOOL_YML"
    exit 1
fi

NEW_CODE=$((CURRENT_CODE + 1))

# Update apktool.yml using sed with flexible whitespace matching
# Matches "versionCode:" followed by any spaces, then the number
sed -i "s/versionCode:[[:space:]]*$CURRENT_CODE/versionCode: $NEW_CODE/" $APKTOOL_YML

echo "Bumped versionCode from $CURRENT_CODE to $NEW_CODE"