angular.module('genome.relatives', [])
.factory('Relatives', function($http){

  getRelatives = function(){
    return $http({
      method: 'GET',
      url: '/user/relativesinfo/'
    })
  }

  return {
    getRelatives: getRelatives
  }
})