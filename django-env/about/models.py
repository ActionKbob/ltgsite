from django.db import models

class Member( models.Model ) :
    first_name = models.CharField( max_length = 25 )
    last_name = models.CharField( max_length = 25 )
    nick_name = models.CharField( max_length = 25, blank = True, null = True )
    title = models.CharField( max_length = 50 )
    description = models.TextField()

    def __unicode__( self ) :
        return '%s' % self.first_name + self.last_name

    def __str__( self ) :
        return self.first_name + " " + self.last_name

    def get_full_name( self ) :
        if self.nick_name :
            return self.first_name + " &quot;" + self.nick_name + "&quot; " + self.last_name
        else :
            return self.first_name + " " + self.last_name
