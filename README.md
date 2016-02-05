# assignments
Template for Assignments

## Checkout an assignment

Note, **Replace** $IU_USERNAME and $HW with real values
:

	git clone git@github.iu.edu:BDOSSPSpring2016/$IU_USERNAME.git
	cd $IU_USERNAME
	git branch $HW
	git checkout $HW
	git pull t@github.iu.edu:BDOSSPSpring2016/assignments.git $HW
	git push -u origin $HW

For example, hw3 with 'albert' IU Username:

	git clone git@github.iu.edu:BDOSSPSpring2016/albert.git
	cd albert
	git branch hw3
	git checkout hw3
	git pull t@github.iu.edu:BDOSSPSpring2016/assignments.git hw3
	git push -u origin hw3


