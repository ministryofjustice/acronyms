#!/bin/zsh

# track this files location so can find where the readme file is
_acronymDirectory=${0:a:h};
# function to search withing the MoJ acronyms read me 
# for term passed
# $1 = term to look for
# $2 = flag match term in any part of document
function acronym () {
    local readmePath="${_acronymDirectory}/../README.md"
    local cols="$(tput cols)"
    if [[ ! -f "${readmePath}" ]]; then
        echo "Cannot find source file '${readmePath}'";    
    fi
    if [[ -z $1 ]]; then
        echo "Usage: ${0} [lookup] [--all]"
        echo "  lookup      acroynm to search for"
        echo "  --all       match anywhere in document, including middle of words (so 'ted' would find 'united') and outside of main table."        
    else 
        local matched=""
        if [[ -z "${2}" ]]; then
            matched="$(grep -i "^| ${1} |" ${readmePath})"
        else
            matched="$(grep -i "${1}" ${readmePath})"
        fi
        if [[ -z "${matched}" ]]; then
            echo "Could not find acronym '${1}' in source '${readmePath}'";
        else 
            local output=$(echo "${matched:1}" | sed 's/|/#/g' | tr '#' '\n')
            echo ${output}
        fi
    fi
}
