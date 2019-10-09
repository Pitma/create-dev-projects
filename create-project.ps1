Param
  (
    [parameter(Position=0)]
    [String[]]
    $projectName
    )
 
cd c:\Development\create-dev-projects
python create-dev-project.py $projectName
