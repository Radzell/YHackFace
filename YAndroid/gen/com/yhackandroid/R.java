/* AUTO-GENERATED FILE.  DO NOT MODIFY.
 *
 * This class was automatically generated by the
 * aapt tool from the resource data it found.  It
 * should not be modified by hand.
 */

package com.yhackandroid;

public final class R {
    public static final class attr {
        /** <p>Must be a reference to another resource, in the form "<code>@[+][<i>package</i>:]<i>type</i>:<i>name</i></code>"
or to a theme attribute in the form "<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>".
         */
        public static final int buttonBarButtonStyle=0x7f010003;
        /** <p>Must be a reference to another resource, in the form "<code>@[+][<i>package</i>:]<i>type</i>:<i>name</i></code>"
or to a theme attribute in the form "<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>".
         */
        public static final int buttonBarStyle=0x7f010002;
        /** <p>May be an integer value, such as "<code>100</code>".
<p>This may also be a reference to a resource (in the form
"<code>@[<i>package</i>:]<i>type</i>:<i>name</i></code>") or
theme attribute (in the form
"<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>")
containing a value of this type.
<p>May be one of the following constant values.</p>
<table>
<colgroup align="left" />
<colgroup align="left" />
<colgroup align="left" />
<tr><th>Constant</th><th>Value</th><th>Description</th></tr>
<tr><td><code>any</code></td><td>-1</td><td></td></tr>
<tr><td><code>back</code></td><td>99</td><td></td></tr>
<tr><td><code>front</code></td><td>98</td><td></td></tr>
</table>
         */
        public static final int camera_id=0x7f010001;
        /** <p>Must be a boolean value, either "<code>true</code>" or "<code>false</code>".
<p>This may also be a reference to a resource (in the form
"<code>@[<i>package</i>:]<i>type</i>:<i>name</i></code>") or
theme attribute (in the form
"<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>")
containing a value of this type.
         */
        public static final int show_fps=0x7f010000;
    }
    public static final class color {
        public static final int black_overlay=0x7f060000;
    }
    public static final class drawable {
        public static final int ic_launcher=0x7f020000;
    }
    public static final class id {
        public static final int any=0x7f050000;
        public static final int back=0x7f050001;
        public static final int fd_activity_surface_view=0x7f050003;
        public static final int front=0x7f050002;
    }
    public static final class layout {
        public static final int activity_main=0x7f030000;
    }
    public static final class raw {
        public static final int lbpcascade_frontalface=0x7f040000;
    }
    public static final class string {
        public static final int app_name=0x7f070000;
        public static final int dummy_button=0x7f070001;
        public static final int dummy_content=0x7f070002;
    }
    public static final class style {
        /** 
        Base application theme, dependent on API level. This theme is replaced
        by AppBaseTheme from res/values-vXX/styles.xml on newer devices.
    

            Theme customizations available in newer API levels can go in
            res/values-vXX/styles.xml, while customizations related to
            backward-compatibility can go here.
        

        Base application theme for API 11+. This theme completely replaces
        AppBaseTheme from res/values/styles.xml on API 11+ devices.
    
 API 11 theme customizations can go here. 

        Base application theme for API 14+. This theme completely replaces
        AppBaseTheme from BOTH res/values/styles.xml and
        res/values-v11/styles.xml on API 14+ devices.
    
 API 14 theme customizations can go here. 
         */
        public static final int AppBaseTheme=0x7f080000;
        /**  Application theme. 
 All customizations that are NOT specific to a particular API-level can go here. 
         */
        public static final int AppTheme=0x7f080001;
        public static final int ButtonBar=0x7f080003;
        public static final int ButtonBarButton=0x7f080004;
        public static final int FullscreenActionBarStyle=0x7f080005;
        public static final int FullscreenTheme=0x7f080002;
    }
    public static final class styleable {
        /** 
         Declare custom theme attributes that allow changing which styles are
         used for button bars depending on the API level.
         ?android:attr/buttonBarStyle is new as of API 11 so this is
         necessary to support previous API levels.
    
           <p>Includes the following attributes:</p>
           <table>
           <colgroup align="left" />
           <colgroup align="left" />
           <tr><th>Attribute</th><th>Description</th></tr>
           <tr><td><code>{@link #ButtonBarContainerTheme_buttonBarButtonStyle com.yhackandroid:buttonBarButtonStyle}</code></td><td></td></tr>
           <tr><td><code>{@link #ButtonBarContainerTheme_buttonBarStyle com.yhackandroid:buttonBarStyle}</code></td><td></td></tr>
           </table>
           @see #ButtonBarContainerTheme_buttonBarButtonStyle
           @see #ButtonBarContainerTheme_buttonBarStyle
         */
        public static final int[] ButtonBarContainerTheme = {
            0x7f010002, 0x7f010003
        };
        /**
          <p>This symbol is the offset where the {@link com.yhackandroid.R.attr#buttonBarButtonStyle}
          attribute's value can be found in the {@link #ButtonBarContainerTheme} array.


          <p>Must be a reference to another resource, in the form "<code>@[+][<i>package</i>:]<i>type</i>:<i>name</i></code>"
or to a theme attribute in the form "<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>".
          @attr name com.yhackandroid:buttonBarButtonStyle
        */
        public static final int ButtonBarContainerTheme_buttonBarButtonStyle = 1;
        /**
          <p>This symbol is the offset where the {@link com.yhackandroid.R.attr#buttonBarStyle}
          attribute's value can be found in the {@link #ButtonBarContainerTheme} array.


          <p>Must be a reference to another resource, in the form "<code>@[+][<i>package</i>:]<i>type</i>:<i>name</i></code>"
or to a theme attribute in the form "<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>".
          @attr name com.yhackandroid:buttonBarStyle
        */
        public static final int ButtonBarContainerTheme_buttonBarStyle = 0;
        /** Attributes that can be used with a CameraBridgeViewBase.
           <p>Includes the following attributes:</p>
           <table>
           <colgroup align="left" />
           <colgroup align="left" />
           <tr><th>Attribute</th><th>Description</th></tr>
           <tr><td><code>{@link #CameraBridgeViewBase_camera_id com.yhackandroid:camera_id}</code></td><td></td></tr>
           <tr><td><code>{@link #CameraBridgeViewBase_show_fps com.yhackandroid:show_fps}</code></td><td></td></tr>
           </table>
           @see #CameraBridgeViewBase_camera_id
           @see #CameraBridgeViewBase_show_fps
         */
        public static final int[] CameraBridgeViewBase = {
            0x7f010000, 0x7f010001
        };
        /**
          <p>This symbol is the offset where the {@link com.yhackandroid.R.attr#camera_id}
          attribute's value can be found in the {@link #CameraBridgeViewBase} array.


          <p>May be an integer value, such as "<code>100</code>".
<p>This may also be a reference to a resource (in the form
"<code>@[<i>package</i>:]<i>type</i>:<i>name</i></code>") or
theme attribute (in the form
"<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>")
containing a value of this type.
<p>May be one of the following constant values.</p>
<table>
<colgroup align="left" />
<colgroup align="left" />
<colgroup align="left" />
<tr><th>Constant</th><th>Value</th><th>Description</th></tr>
<tr><td><code>any</code></td><td>-1</td><td></td></tr>
<tr><td><code>back</code></td><td>99</td><td></td></tr>
<tr><td><code>front</code></td><td>98</td><td></td></tr>
</table>
          @attr name com.yhackandroid:camera_id
        */
        public static final int CameraBridgeViewBase_camera_id = 1;
        /**
          <p>This symbol is the offset where the {@link com.yhackandroid.R.attr#show_fps}
          attribute's value can be found in the {@link #CameraBridgeViewBase} array.


          <p>Must be a boolean value, either "<code>true</code>" or "<code>false</code>".
<p>This may also be a reference to a resource (in the form
"<code>@[<i>package</i>:]<i>type</i>:<i>name</i></code>") or
theme attribute (in the form
"<code>?[<i>package</i>:][<i>type</i>:]<i>name</i></code>")
containing a value of this type.
          @attr name com.yhackandroid:show_fps
        */
        public static final int CameraBridgeViewBase_show_fps = 0;
    };
}
