# Deploy zip to artifact repo with grunt-maven-tasks

###### Configure grunt<sub>~maven</sub>~tasks 

Release and deploy is supported, but only for zip files, not jar. 

- Install 
    - `npm install grunt<sub>~maven</sub>~tasks --save-dev`

- Add to _grunt.initConfig({_ section in _GruntFile.js_: 
```
maven: {
    options: { groupId: 'com.example.project', artifactId: 'artifact-project' },
    deploy: {
        options: { url: 'http://mvnrepo.example.com:8081/nexus/content/repositories/snapshots/', repositoryId: 'example-snapshots' },
        src: [ '**', '!node_modules/**' ]
    },
    release: {
        options: { url: 'http://mvnrepo.example.com:8081/nexus/content/repositories/releases/', repositoryId: 'example-releases', mode: 'minor' },
        src: [ '**', '!node_modules/**' ]
    }
}
```

```
grunt.loadNpmTasks('grunt-maven-tasks');
grunt.registerTask('deploy', [ 'clean', 'test', 'maven:deploy' ]);
grunt.registerTask('release', [ 'clean', 'test', 'maven:release' ]);
```

- In package.json 
```
{
  "name": "artifactproject",
  "version": "0.1-SNAPSHOT",
  "dependencies": {},
  "devDependencies": {
    "grunt": "^0.4.1",
    
    "grunt-maven-tasks": "^1.2.0",
        
  },
  
}
```

###### Build and deploy zip to maven artifact repo 
```
grunt
grunt maven:deploy
```
