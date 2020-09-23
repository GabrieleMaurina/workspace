#include <stdlib.h>
#include <GL/glew.h>
#include <GLFW/glfw3.h>

void key_callback(GLFWwindow* window, int key, int scancode, int action, int mods)
{
	if (key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
		glfwSetWindowShouldClose(window, GLFW_TRUE);
}

int main(int argc, char** argv)
{
	if (!glfwInit()) exit(EXIT_FAILURE);

	GLFWmonitor* monitor = glfwGetPrimaryMonitor();
	const GLFWvidmode* mode = glfwGetVideoMode(monitor);
	const int SCREEN_WIDTH = mode->width;
	const int SCREEN_HEIGHT = mode->height;
	GLFWwindow* window = glfwCreateWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Extreme Voxel", monitor, NULL);

	if (!window){
		glfwTerminate();
		exit(EXIT_FAILURE);
	}

	glfwMakeContextCurrent(window);

	glfwSetKeyCallback(window, key_callback);

    float vertices[] =
    {
        300, 300, 0.0, // top right corner
        0, 300, 0.0, // top left corner
        0, 0, 0.0, // bottom left corner
        300, 0, 0.0, // bottom right corner
        600, 600, 0.0, // top right corner
        300, 600, 0.0, // top left corner
        300, 300, 0.0, // bottom left corner
        600, 300, 0.0 // bottom right corner
    };

    glViewport(0.0f, 0.0f, SCREEN_WIDTH, SCREEN_HEIGHT); // specifies the part of the window to which OpenGL will draw (in pixels), convert from normalised to pixels
    glMatrixMode(GL_PROJECTION); // projection matrix defines the properties of the camera that views the objects in the world coordinate frame. Here you typically set the zoom factor, aspect ratio and the near and far clipping planes
    glLoadIdentity( ); // replace the current matrix with the identity matrix and starts us a fresh because matrix transforms such as glOrpho and glRotate cumulate, basically puts us at (0, 0, 0)
    glOrtho(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT, 0, 1); // essentially set coordinate system
    glMatrixMode(GL_MODELVIEW); // (default matrix mode) modelview matrix defines how your objects are transformed (meaning translation, rotation and scaling) in your world
    glLoadIdentity();

	while (!glfwWindowShouldClose(window)){
		glClear(GL_COLOR_BUFFER_BIT);

        glEnableClientState(GL_VERTEX_ARRAY); // tell OpenGL that you're using a vertex array for fixed-function attribute
        glVertexPointer(3, GL_FLOAT, 0, vertices); // point to the vertices to be used
        glDrawArrays(GL_QUADS, 0, 8); // draw the vertixes
        glDisableClientState(GL_VERTEX_ARRAY); // tell OpenGL that you're finished using the vertex arrayattribute

		glfwSwapBuffers(window);
		glfwPollEvents();
	}

	glfwTerminate();
	exit(EXIT_SUCCESS);
}
